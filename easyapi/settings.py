from .credentials.auth import JSONAuthenticator
from .iotypemodel.iotype_model import IOTypeStack
from .algorithmodel.algorithm_stack import AlgorithmStack
from .taskmodel.taskqueue import TaskQueue

authenticator = JSONAuthenticator('credentials.json')
iolib = IOTypeStack(path='iolib.json')
algorithmlib = AlgorithmStack(
    'algorithms/proteins/select_chain/entry.py',
    'algorithms/proteins/sasa/entry.py',
    iolib=iolib
)
taskqueue = TaskQueue(resources={'cpu':4, 'cuda':0}, algorithmlib=algorithmlib)