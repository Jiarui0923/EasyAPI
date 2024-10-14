from .task import Task
from .taskqueue import TaskQueue

import time

def task_holder(task_queue:TaskQueue, task:Task):
    task_queue.enqueue(task)
    while task_queue.header.task_id != task.task_id: time.sleep(0.05)
    task = task_queue.dequeue()
    task_queue.execute(task)
    task_queue.done_queue.append(task)