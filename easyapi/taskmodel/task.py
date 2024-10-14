from uuid import uuid4
from datetime import datetime,timezone

class Task(object):
    
    def __init__(self, access_id='', algorithm_id='', input_data={}, required_resources={}):
        self.task_id = str(uuid4())
        self.access_id = access_id
        self.algorithm_id = algorithm_id
        self.input_data = input_data
        self.output_data = None
        self.in_progress = False
        self.is_done = False
        self.required_resources = required_resources
        self.create_time = self._get_time()
        self.start_time = None
        self.done_time = None
        self.error = None
        
    def __repr__(self): return f'<({self.create_time}){self.task_id} is_done:{self.is_done}>'
        
    def _get_time(self): return datetime.now(timezone.utc)
    
    def _execute_start(self):
        self.in_progress = True
        self.start_time = self._get_time()
    def _execute_end(self):
        self.in_progress = False
        self.is_done = True
        self.done_time = self._get_time()
    
    def execute(self, algorithmlib, resources={}):
        self._execute_start()
        algorithm = algorithmlib[self.algorithm_id]
        succ, output = algorithm(self.input_data, resources=resources)
        if not succ: self.error = output
        else: self.output_data = output
        self._execute_end()
        return output
        
        
        