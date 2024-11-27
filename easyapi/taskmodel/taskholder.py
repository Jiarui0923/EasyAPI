from .task import Task
from .taskqueue import TaskQueue

import time
import asyncio

async def _task_runner(task_queue:TaskQueue, task:Task):
    try:
        while not task_queue.is_header(task): await asyncio.sleep(0.05)
        task_queue.execute(task)
        task = task_queue.dequeue(task)
        task_queue.done_queue.append(task)
    except asyncio.CancelledError: return
    

def task_holder(task_queue:TaskQueue, task:Task):
    _asyncio_task = asyncio.create_task(_task_runner(task_queue=task_queue, task=task))
    task._asyncio_task = _asyncio_task
    task_queue.enqueue(task)
    