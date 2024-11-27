from .task import Task
import pandas as pd
import numpy as np
import os

class TaskQueue(object):
    
    def __init__(self, queue_configs=[{'cpu':os.cpu_count(), 'cuda':0}], algorithmlib=None):
        self.queues = [(queue_config, []) for queue_config in queue_configs]
        self.resource_matrix = pd.DataFrame(queue_configs, dtype=float)
        self.done_queue = []
        self.algorithmlib = algorithmlib
        
    def __len__(self): return len(self.queue)
    
    def queue_where(self, task):
        for (_, queue) in self.queues:
            for pos, task_ in enumerate(queue):
                if task_.task_id == task.task_id: return pos+1
    
    def __getitem__(self, task_id):
        for (_, queue) in self.queues:
            for task in queue:
                if task.task_id == task_id: return task
        for task in self.done_queue:
            if task.task_id == task_id: return task
        return None
    def __delitem__(self, task_id):
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
        task_id = task.task_id
        for (_, queue) in self.queues:
            if len(queue) > 0 and task_id == queue[0].task_id: return True
        return False
    
    def resource_distance(self, resources):
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
        _required_resources = task.required_resources
        queue_id = self.resource_distance(_required_resources)
        self.queues[queue_id][1].append(task)
        
    def dequeue(self, task):
        for (_, queue) in self.queues:
            if len(queue) > 0 and task.task_id == queue[0].task_id:
                del queue[0]
        return task
    
    def execute(self, task):
        for (resource, queue) in self.queues:
            if len(queue) > 0 and task.task_id == queue[0].task_id:
                return task.execute(algorithmlib=self.algorithmlib, resources=resource)