
from .algorithmodel.algorithm_stack import AlgorithmStack

import os

def load_config(path):
    import json
    with open(path, 'r') as conf_f: return json.load(conf_f)
_path = os.environ.get('easyapi_config', 'config.json')
_conf = load_config(_path)

modules = _conf.get('modules', None)
for module in modules: __import__(module)

def _build_authenticator(_auth_conf:dict):
    _type = _auth_conf.get('type', 'json')
    if _type == 'json':
        from .credentials.auth import JSONAuthenticator
        return JSONAuthenticator(_auth_conf.get('file', 'credentials.json'))
    elif _type == 'memory':
        from .credentials.auth import Authenticator
        return Authenticator(_auth_conf.get('credentials', {}))
    else: raise TypeError(f'{_type} Not Supported for Authenticator.')
authenticator = _build_authenticator(_conf.get('authenticator', {'type': 'memory'}))

def _build_iotype_stack(_iostack_conf):
    from .iotypemodel.iotype_model import IOTypeStack
    return IOTypeStack(path=_iostack_conf.get('file', 'iolib.json'))
iolib = _build_iotype_stack(_conf.get('iolib', {}))

entries = []
algorithmlib = AlgorithmStack(
    *entries,
    iolib=iolib
)

def _build_task_queue(_task_queue_conf):
    from .taskmodel.taskqueue import TaskQueue
    return TaskQueue(queue_configs=_task_queue_conf.get('layouts', [{'cuda':0, 'cpu':1},
                                                                    {'cuda':0, 'cpu':os.cpu_count()-1}]),
                     algorithmlib=algorithmlib)
taskqueue = _build_task_queue(_conf.get('task_queue', {}))

server_name = _conf.get('server_name', 'local_server')

def _config_cache(_cache_config):
    from .algorithmodel.cache import AlgorithmCachePool
    from .algorithmodel.cache import Storage
    _type = _cache_config.get('type', 'memory')
    if _type == 'mongodb':
        AlgorithmCachePool.engine(Storage.MongoDB(host=_cache_config.get('host', 'mongodb://localhost'),
                                                  database=_cache_config.get('database', 'easyapi_cache')),
                                  hash=_cache_config.get('hash', 'MD5'))
    elif _type == 'memory':
        AlgorithmCachePool.engine(Storage.Memory(),
                                  hash=_cache_config.get('hash', 'MD5'))
    else: raise TypeError(f'{_type} Not Supported for Cache.')
_config_cache(_conf.get('cache', {}))