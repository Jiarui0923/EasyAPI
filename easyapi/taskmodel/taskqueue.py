from .task import Task

class TaskQueue(object):
    
    def __init__(self, resources={}, algorithmlib=None):
        self.resources = resources
        self.queue = []
        self.done_queue = []
        self.algorithmlib = algorithmlib
        
    def __len__(self): return len(self.queue)
    
    def queue_where(self, task):
        pos = 0
        for task_ in self.queue:
            if task_.task_id != task.task_id: pos += 1
            else: return pos
    
    def __getitem__(self, task_id):
        for task in self.queue:
            if task.task_id == task_id: return task
        for task in self.done_queue:
            if task.task_id == task_id: return task
        return None
    def __delitem__(self, task_id):
        for i in range(len(self.done_queue)):
            if task_id == self.done_queue[i].task_id:
                del self.done_queue[i]
                return
        for i in range(len(self.queue)):
            if task_id == self.queue[i].task_id:
                if self.queue[i].in_progress: raise RuntimeError('Task is running')
                del self.queue[i]
                return
        raise LookupError('Task not found')
    
    
    @property
    def header(self): return self.queue[0]
    
    def enqueue(self, task):
        self.queue.append(task)
        
    def dequeue(self):
        task = self.queue[0]
        del self.queue[0]
        return task
    
    def execute(self, task):
        return task.execute(algorithmlib=self.algorithmlib, resources=self.resources)