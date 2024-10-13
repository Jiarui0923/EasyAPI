from fastapi import APIRouter
from ..settings import authenticator

route = APIRouter(prefix='/tasks')

@route.get('/{task_id}')
def get_task(task_id): pass

@route.post('/{task_id}/cancel')
def cancel_task(task_id): pass

