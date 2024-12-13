"""
Task Management and Execution Module
-------------------------------------

This module defines functions and an asynchronous runner to handle task execution within a task queue. It uses
asyncio to manage the scheduling and execution of tasks in an efficient, non-blocking manner. The tasks are executed
with the help of a thread pool executor and managed within a task queue.

Functions:
----------
_task_runner(task_queue: TaskQueue, task: Task)
    An asynchronous function that runs the given task when it becomes the first task in the queue.
    
task_holder(task_queue: TaskQueue, task: Task)
    A function that adds the task to the task queue and initiates the asynchronous task runner.
"""

from .task import Task
from .taskqueue import TaskQueue
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Executor for running tasks in a separate thread.
executor = ThreadPoolExecutor()

async def _task_runner(task_queue: TaskQueue, task: Task):
    """
    An asynchronous function that runs the given task when it becomes the first task in the queue.
    
    This function waits for the task to be the first in the queue, executes it using a thread pool executor, and 
    then moves the task to the done queue after completion.
    
    Parameters:
    ----------
    task_queue : TaskQueue
        The task queue containing the tasks.
    task : Task
        The task to be executed.
    
    Raises:
    ------
    asyncio.CancelledError
        If the task is cancelled during execution.
    """
    try:
        # Wait until the task becomes the first task in the queue.
        while not task_queue.is_header(task):
            await asyncio.sleep(0.1)
        
        # Get the event loop and run the task using the executor.
        loop = asyncio.get_event_loop()

        def _run_task():
            """
            Helper function to execute the task using the executor.
            """
            task_queue.execute(task)
        
        # Run the task in a separate thread.
        await loop.run_in_executor(executor, _run_task)

        # Wait for the task execution to finish (loop will run forever in this case).
        await loop.run_forever()

        # Dequeue the task and move it to the done queue after completion.
        task = task_queue.dequeue(task)
        task_queue.done_queue.append(task)
    except asyncio.CancelledError:
        # Handle task cancellation
        return

def task_holder(task_queue: TaskQueue, task: Task):
    """
    A function that adds the task to the task queue and initiates the asynchronous task runner.
    
    This function schedules the execution of the task by creating an asyncio task and assigning it to the task queue.
    
    Parameters:
    ----------
    task_queue : TaskQueue
        The task queue to which the task will be added.
    task : Task
        The task to be held and executed.
    """
    # Create an asyncio task to run the task asynchronously.
    _asyncio_task = asyncio.create_task(_task_runner(task_queue=task_queue, task=task))
    
    # Store the asyncio task reference in the task object.
    task._asyncio_task = _asyncio_task
    
    # Add the task to the task queue for scheduling.
    task_queue.enqueue(task)
