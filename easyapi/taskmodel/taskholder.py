from .task import Task
from .taskqueue import TaskQueue

import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()
async def _task_runner(task_queue:TaskQueue, task:Task):
    try:
        while not task_queue.is_header(task): await asyncio.sleep(0.1)
        loop = asyncio.get_event_loop()
        def _run_task():
            task_queue.execute(task)
        await loop.run_in_executor(executor, _run_task)
        await loop.run_forever()
        # task_queue.execute(task)
        task = task_queue.dequeue(task)
        task_queue.done_queue.append(task)
    except asyncio.CancelledError: return
    
def task_holder(task_queue:TaskQueue, task:Task):
    _asyncio_task = asyncio.create_task(_task_runner(task_queue=task_queue, task=task))
    task._asyncio_task = _asyncio_task
    task_queue.enqueue(task)
    