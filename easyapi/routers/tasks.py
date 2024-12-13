"""
FastAPI Routes for Task Management
------------------------------------

This module defines API routes for managing tasks. It includes endpoints for retrieving task status,
managing WebSocket connections for real-time updates on task progress, and canceling tasks. The routes are 
secured with user authentication via the `authenticator` dependency and interact with the `taskqueue` for task management.

Routes:
-------
- GET /tasks/{task_id}: Retrieves the status of a specific task.
- POST /tasks/{task_id}/cancel: Cancels a task if it is not yet completed.
- WebSocket /tasks/{task_id}/ws: Establishes a WebSocket connection for real-time updates of a task's progress.

Classes:
--------
ConnectionManager:
    Manages WebSocket connections for task progress updates.

Functions:
----------
build_task_response(task_id, task)
    Constructs a dictionary response containing the current status of a task.
    
get_task(task_id, auth_id)
    Retrieves and returns the status of a specific task.

manage_task_ws(websocket, task_id, auth_id)
    Manages a WebSocket connection for real-time task updates.
    
cancel_task(task_id, auth_id)
    Cancels a task and removes it from the task queue.

"""

from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect, WebSocketException, status
import json
from ..settings import authenticator
from ..settings import taskqueue

# Initialize FastAPI router with the 'tasks' prefix
route = APIRouter(prefix='/tasks')

def build_task_response(task_id, task):
    """
    Constructs a dictionary response containing the current status of a task.
    
    Parameters:
    ----------
    task_id : str
        The ID of the task to retrieve the status for.
    task : Task
        The task object containing information about the task's state.
    
    Returns:
    -------
    dict
        A dictionary containing the task's status and related information.
    """
    if task.is_done:
        response = {
            'task_id': task.task_id,
            'algorithm': task.algorithm_id,
            'create_time': task.create_time,
            'start_time': task.start_time,
            'done_time': task.done_time,
            'success': task.error is None,
            'output': task.output_data if task.error is None else task.error,
        }
        del taskqueue[task_id]
    else:
        if task.in_progress:
            response = {
                'task_id': task.task_id,
                'status': 'in-progress',
                'create_time': task.create_time,
                'start_time': task.start_time,
            }
        else:
            response = {
                'task_id': task.task_id,
                'status': 'in-queue',
                'create_time': task.create_time,
                'queue_length': taskqueue.queue_where(task=task)
            }
    return response

@route.get('/{task_id}')
async def get_task(task_id, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves and returns the status of a specific task.
    
    Parameters:
    ----------
    task_id : str
        The ID of the task to retrieve.
    auth_id : str
        The ID of the user making the request, used for authorization.
        
    Returns:
    -------
    dict
        A dictionary containing the task's status and related information.
    
    Raises:
    ------
    HTTPException
        If the task is not found or if the user is not authorized to view the task.
    """
    task = taskqueue[task_id]
    if task is None:
        raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    if task.access_id != auth_id:
        raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    return build_task_response(task_id, task)

class ConnectionManager:
    """
    Manages WebSocket connections for task progress updates.
    
    Attributes:
    ----------
    active_connections : list
        A list of active WebSocket connections.
    
    Methods:
    -------
    connect(websocket: WebSocket)
        Accepts a WebSocket connection and adds it to the active connections list.
        
    disconnect(websocket: WebSocket)
        Removes a WebSocket connection from the active connections list.
        
    send_message(message: str, websocket: WebSocket)
        Sends a message to a specific WebSocket connection.
    """
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Accepts a WebSocket connection and adds it to the active connections list.
        
        Parameters:
        ----------
        websocket : WebSocket
            The WebSocket connection to accept.
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
        Removes a WebSocket connection from the active connections list.
        
        Parameters:
        ----------
        websocket : WebSocket
            The WebSocket connection to disconnect.
        """
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        """
        Sends a message to a specific WebSocket connection.
        
        Parameters:
        ----------
        message : str
            The message to send to the WebSocket connection.
        websocket : WebSocket
            The WebSocket connection to send the message to.
        """
        await websocket.send_text(message)

# Instantiate the WebSocket connection manager
ws_manager = ConnectionManager()

@route.websocket('/{task_id}/ws')
async def manage_task_ws(websocket: WebSocket, task_id, auth_id: str = Depends(authenticator.url_auth)):
    """
    Manages a WebSocket connection for real-time task updates.
    
    Parameters:
    ----------
    websocket : WebSocket
        The WebSocket connection for real-time communication.
    task_id : str
        The ID of the task to track.
    auth_id : str
        The ID of the user making the request, used for authorization.
    """
    await ws_manager.connect(websocket)
    try:
        while True:
            command = await websocket.receive_text()
            if command.lower() == 'get':
                task = taskqueue[task_id]
                if task is None or task.access_id != auth_id:
                    await ws_manager.send_message(
                        json.dumps({'status': f'Task {task_id} not found', 'success': False}), websocket
                    )
                else:
                    await ws_manager.send_message(
                        json.dumps(build_task_response(task_id, task), default=str), websocket
                    )
            else:
                await ws_manager.send_message(
                    json.dumps({'status': f'{command} not supported.', 'success': False}), websocket
                )
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except WebSocketException:
        ws_manager.disconnect(websocket)

@route.post('/{task_id}/cancel')
async def cancel_task(task_id, auth_id: str = Depends(authenticator.url_auth)):
    """
    Cancels a task and removes it from the task queue.
    
    Parameters:
    ----------
    task_id : str
        The ID of the task to cancel.
    auth_id : str
        The ID of the user making the request, used for authorization.
    
    Returns:
    -------
    dict
        A dictionary containing the task ID and a success flag.
    
    Raises:
    ------
    HTTPException
        If the task is not found or if the user is not authorized to cancel the task.
    """
    task = taskqueue[task_id]
    if task is None:
        raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    if task.access_id != auth_id:
        raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    # Remove the task from the queue
    del taskqueue[task_id]
    return {'task_id': task.task_id, 'success': True}
