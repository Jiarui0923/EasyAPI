"""
Task Queue Management Module
-----------------------------

This module defines the `TaskQueue` class, which manages a queue of computational tasks. It handles task scheduling,
resource allocation, task execution, and tracking task statuses. The class provides functionality for managing
multiple task queues with different resource configurations and assigning tasks to the appropriate queues based on
resource requirements.

Classes:
--------
TaskQueue
    A class that manages a queue of tasks, resource allocation, and task execution.

Methods:
--------
__init__(self, queue_configs=[{'cpu':os.cpu_count(), 'cuda':0}], algorithmlib=None)
    Initializes the task queue with the given configurations and algorithm library.

__len__(self)
    Returns the number of queues in the task queue.

queue_where(self, task)
    Returns the position of the given task in the queue.

__getitem__(self, task_id)
    Retrieves the task with the specified task ID from the queue or the done queue.

__delitem__(self, task_id)
    Deletes the task with the specified task ID from the queue or done queue.

is_header(self, task)
    Checks if the task is the first task in any of the queues.

resource_distance(self, resources)
    Calculates the resource distance for task scheduling and returns the queue ID with the minimum resource distance.

enqueue(self, task)
    Adds a task to the appropriate queue based on its resource requirements.

dequeue(self, task)
    Removes a task from the queue and returns it.

execute(self, task)
    Executes the specified task using the available resources and algorithm library.
"""

from .task import Task
import pandas as pd
import numpy as np
import os


class TaskQueue(object):
    """
    A class that manages a queue of tasks, resource allocation, and task execution.

    Attributes:
    ----------
    queues : list of tuples
        A list of queues, each containing resource configurations and the associated tasks.
    resource_matrix : pandas.DataFrame
        A matrix of resources and their quantities available in the system.
    done_queue : list
        A list of tasks that have completed execution.
    algorithmlib : dict
        A dictionary of available algorithms for executing tasks.
    """
    
    def __init__(self, queue_configs=[{'cpu': os.cpu_count(), 'cuda': 0}], algorithmlib=None):
        """
        Initializes the task queue with the given configurations and algorithm library.
        
        Parameters:
        ----------
        queue_configs : list of dicts, optional
            A list of dictionaries representing resource configurations for each queue (default is CPU and CUDA configurations).
        algorithmlib : dict, optional
            A dictionary of algorithms available for task execution (default is None).
        """
        self.queues = [(queue_config, []) for queue_config in queue_configs]
        self.resource_matrix = pd.DataFrame(queue_configs, dtype=float)
        self.done_queue = []
        self.algorithmlib = algorithmlib
    
    def __len__(self):
        """
        Returns the number of queues in the task queue.
        
        Returns:
        -------
        int
            The number of queues in the task queue.
        """
        return len(self.queues)
    
    def queue_where(self, task):
        """
        Returns the position of the given task in the queue.
        
        Parameters:
        ----------
        task : Task
            The task whose position is to be found in the queue.
        
        Returns:
        -------
        int
            The position of the task in the queue (1-based index).
        """
        for (_, queue) in self.queues:
            for pos, task_ in enumerate(queue):
                if task_.task_id == task.task_id:
                    return pos + 1
    
    def __getitem__(self, task_id):
        """
        Retrieves the task with the specified task ID from the queue or the done queue.
        
        Parameters:
        ----------
        task_id : str
            The ID of the task to retrieve.
        
        Returns:
        -------
        Task or None
            The task with the specified task ID, or None if the task is not found.
        """
        for (_, queue) in self.queues:
            for task in queue:
                if task.task_id == task_id:
                    return task
        for task in self.done_queue:
            if task.task_id == task_id:
                return task
        return None
    
    def __delitem__(self, task_id):
        """
        Deletes the task with the specified task ID from the queue or done queue.
        
        Parameters:
        ----------
        task_id : str
            The ID of the task to delete.
        
        Raises:
        ------
        LookupError
            If the task is not found in any of the queues or the done queue.
        """
        for i in range(len(self.done_queue)):
            if task_id == self.done_queue[i].task_id:
                del self.done_queue[i]
                return
        for (_, queue) in self.queues:
            for i in range(len(queue)):
                if task_id == queue[i].task_id:
                    queue[i].cancel()
                    del queue[i]
                    return
        raise LookupError('Task not found')
    
    def is_header(self, task):
        """
        Checks if the task is the first task in any of the queues.
        
        Parameters:
        ----------
        task : Task
            The task to check.
        
        Returns:
        -------
        bool
            True if the task is the first task in the queue, False otherwise.
        """
        task_id = task.task_id
        for (_, queue) in self.queues:
            if len(queue) > 0 and task_id == queue[0].task_id:
                return True
        return False
    
    def resource_distance(self, resources):
        """
        Calculates the resource distance for task scheduling and returns the queue ID with the minimum resource distance.
        
        Parameters:
        ----------
        resources : dict
            A dictionary of resource names and quantities required by the task.
        
        Returns:
        -------
        int
            The queue ID (index) with the minimum resource distance.
        """
        _dis = self.resource_matrix.copy(deep=True)
        for resource_name, resource_quantity in resources.items():
            if resource_quantity == -1:
                resource_quantity = self.resource_matrix[resource_name].max()
            _dis[resource_name] = resource_quantity - _dis[resource_name]
            if resource_quantity != 0:
                _dis.loc[self.resource_matrix[resource_name] == 0, resource_name] = np.inf
        _dis = np.abs(np.nansum(_dis.values, axis=1))
        _queue_id = np.argmin(_dis)
        return _queue_id
    
    def enqueue(self, task):
        """
        Adds a task to the appropriate queue based on its resource requirements.
        
        Parameters:
        ----------
        task : Task
            The task to enqueue.
        """
        _required_resources = task.required_resources
        queue_id = self.resource_distance(_required_resources)
        self.queues[queue_id][1].append(task)
    
    def dequeue(self, task):
        """
        Removes a task from the queue and returns it.
        
        Parameters:
        ----------
        task : Task
            The task to dequeue.
        
        Returns:
        -------
        Task
            The dequeued task.
        """
        for (_, queue) in self.queues:
            if len(queue) > 0 and task.task_id == queue[0].task_id:
                del queue[0]
        return task
    
    def execute(self, task):
        """
        Executes the specified task using the available resources and algorithm library.
        
        Parameters:
        ----------
        task : Task
            The task to execute.
        
        Returns:
        -------
        object
            The output data generated by the task after execution.
        """
        for (resource, queue) in self.queues:
            if len(queue) > 0 and task.task_id == queue[0].task_id:
                return task.execute(algorithmlib=self.algorithmlib, resources=resource)
