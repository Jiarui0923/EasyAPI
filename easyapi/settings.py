from .credentials.auth import JSONAuthenticator
from .iotypemodel.iotype_model import IOTypeStack
from .algorithmodel.algorithm_stack import AlgorithmStack
from .taskmodel.taskqueue import TaskQueue

authenticator = JSONAuthenticator('credentials.json')
iolib = IOTypeStack(path='iolib.json')
algorithmlib = AlgorithmStack(
    # 'algorithms/add_number.py',
    'algorithms/proteins/select_chain/entry.py',
    'algorithms/proteins/sasa/entry.py',
    'algorithms/proteins/corex/entry.py',
    'algorithms/proteins/list_chain/entry.py',
    'algorithms/proteins/bfactor/entry.py',
    'algorithms/proteins/get_pdb/entry.py',
    iolib=iolib
)
taskqueue = TaskQueue(resources={'cpu':4, 'cuda':0}, algorithmlib=algorithmlib)
server_name = 'Local Test Server'