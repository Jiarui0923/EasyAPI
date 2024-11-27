from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect, WebSocketException, status
import json
from ..settings import authenticator
from ..settings import taskqueue

route = APIRouter(prefix='/tasks')

def build_task_response(task_id, task):
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
async def get_task(task_id, auth_id : str = Depends(authenticator.url_auth)):
    task = taskqueue[task_id]
    if task is None: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    if task.access_id != auth_id: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    return build_task_response(task_id, task)
    

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


ws_manager = ConnectionManager()


@route.websocket('/{task_id}/ws')
async def manage_task_ws(websocket: WebSocket, task_id, auth_id : str = Depends(authenticator.url_auth)):
    await ws_manager.connect(websocket)
    try:
        while True:
            command = await websocket.receive_text()
            if command.lower() == 'get':
                task = taskqueue[task_id]
                if task is None or task.access_id != auth_id:
                    await ws_manager.send_message(json.dumps({'status': f'Task {task_id} not found', 'success': False}), websocket)
                else:
                    await ws_manager.send_message(json.dumps(build_task_response(task_id, task), default=str), websocket)
            else:
                await ws_manager.send_message(json.dumps({'status': f'{command} not supports.', 'success': False}), websocket)
    except WebSocketDisconnect: ws_manager.disconnect(websocket)
    except WebSocketException: ws_manager.disconnect(websocket)

@route.post('/{task_id}/cancel')
async def cancel_task(task_id, auth_id : str = Depends(authenticator.url_auth)):
    task = taskqueue[task_id]
    if task is None: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    if task.access_id != auth_id: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    # if task.in_progress: return {'task_id': task.task_id, 'success': False, 'info': 'Task is in-progress'}
    del taskqueue[task_id]
    return {'task_id': task.task_id, 'success': True}

