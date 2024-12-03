from .credentials.auth import JSONAuthenticator
from .iotypemodel.iotype_model import IOTypeStack
from .algorithmodel.algorithm_stack import AlgorithmStack
from .algorithmodel.cache import AlgorithmCachePool
from .algorithmodel.cache import Storage
from .taskmodel.taskqueue import TaskQueue

__import__('algorithms')

authenticator = JSONAuthenticator('credentials.json')
iolib = IOTypeStack(path='iolib.json')
algorithmlib = AlgorithmStack(
    # 'algorithms/add_number.py',
    'algorithms/proteins/select_chain/entry.py',
    'algorithms/proteins/sasa/entry.py',
    # 'algorithms/proteins/corex/entry.py',
    'algorithms/proteins/list_chain/entry.py',
    'algorithms/proteins/bfactor/entry.py',
    'algorithms/proteins/get_pdb/entry.py',
    'algorithms/proteins/get_seq/entry.py',
    iolib=iolib
)

taskqueue = TaskQueue(queue_configs=[{'cpu':1, 'cuda':0},
                                     {'cpu':3, 'cuda':0}],
                      algorithmlib=algorithmlib)
server_name = 'Local Test Server'
AlgorithmCachePool.engine(Storage.MongoDB(database='easyapi_cache'), hash='MD5')