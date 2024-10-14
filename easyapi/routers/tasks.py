from fastapi import APIRouter, Depends, HTTPException
from ..settings import authenticator
from ..settings import taskqueue

route = APIRouter(prefix='/tasks')

@route.get('/{task_id}')
async def get_task(task_id, auth_id : str = Depends(authenticator.url_auth)):
    task = taskqueue[task_id]
    if task is None: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    if task.access_id != auth_id: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
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

@route.post('/{task_id}/cancel')
async def cancel_task(task_id, auth_id : str = Depends(authenticator.url_auth)):
    task = taskqueue[task_id]
    if task is None: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    if task.access_id != auth_id: raise HTTPException(status_code=404, detail=f'Task {task_id} not found')
    
    if task.in_progress: return {'task_id': task.task_id, 'success': False, 'info': 'Task is in-progress'}
    del taskqueue[task_id]
    return {'task_id': task.task_id, 'success': True}

