from .task import Task

class TaskQueue(object):
    
    def __init__(self, resources={}, algorithmlib=None):
        self.resources = resources
        self.queue = []
        self.done_queue = []
        self.algorithmlib = algorithmlib
        
    def __len__(self): return len(self.queue)
    def __getitem__(self, task_id):
        for task in self.queue:
            if task.task_id == task_id: return task
        return None
    
    
    def enqueue(self, access_id='', algorithm_id='', input_data={}, required_resources={}):
        task = Task(access_id=access_id, algorithm_id=algorithm_id,
                    input_data=input_data, required_resources=required_resources)
        self.queue.append(task)
        
    def dequeue(self):
        task = self.queue[0]
        del self.queue[0]
        return task