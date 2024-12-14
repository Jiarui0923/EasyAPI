"""
Configuration and Initialization Module for EasyAPI
---------------------------------------------------

This module is responsible for loading configuration, initializing components like authenticator, 
IO type stack, algorithm stack, task queue, and cache. It reads configuration from a file 
(defined by the 'easyapi_config' environment variable) and uses it to set up the system.

Components:
-----------
- Authenticator: Manages user authentication, supporting JSON and in-memory types.
- IOTypeStack: Handles IO type configurations.
- AlgorithmStack: Initializes the algorithm stack used by the system.
- TaskQueue: Configures the task queue, supporting layouts for task distribution.
- Cache: Configures the caching system using either MongoDB or in-memory storage.

Dependencies:
------------
- `AlgorithmStack`: Handles the algorithm-related operations.
- `IOTypeStack`: Defines the stack of IO types.
- `TaskQueue`: Manages the task queue and its layouts.
- `Authenticator`: Provides authentication services based on configuration.
- `AlgorithmCachePool` and `Storage`: Handle caching, supporting both MongoDB and memory storage.
"""

import os
import json
from .algorithmodel.algorithm_stack import AlgorithmStack


def load_config(path):
    """
    Loads the configuration from a specified JSON file.

    Parameters:
    ----------
    path : str
        The path to the JSON configuration file.

    Returns:
    -------
    dict
        The parsed configuration data from the file.
    """
    with open(path, 'r') as conf_f:
        return json.load(conf_f)


# Load configuration from environment variable or default to 'config.json'
_path = os.environ.get('easyapi_config', 'config.json')
_conf = load_config(_path)

# Import specified modules from the configuration
modules = _conf.get('modules', None)
for module in modules:
    __import__(module)


def _build_authenticator(_auth_conf: dict):
    """
    Builds and returns the authenticator based on the configuration.

    Parameters:
    ----------
    _auth_conf : dict
        The configuration dictionary for the authenticator.

    Returns:
    -------
    Authenticator
        The initialized authenticator instance.
    
    Raises:
    ------
    TypeError
        If the specified authenticator type is not supported.
    """
    _type = _auth_conf.get('type', 'json')
    if _type == 'json':
        from .credentials.auth import JSONAuthenticator
        return JSONAuthenticator(_auth_conf.get('file', 'credentials.json'))
    elif _type == 'memory':
        from .credentials.auth import Authenticator
        return Authenticator(_auth_conf.get('credentials', {}))
    else:
        raise TypeError(f'{_type} Not Supported for Authenticator.')


# Initialize the authenticator using the configuration
authenticator = _build_authenticator(_conf.get('authenticator', {'type': 'memory'}))


def _build_iotype_stack(_iostack_conf):
    """
    Builds and returns the IO type stack based on the configuration.

    Parameters:
    ----------
    _iostack_conf : dict
        The configuration dictionary for the IO type stack.

    Returns:
    -------
    IOTypeStack
        The initialized IO type stack instance.
    """
    from .iotypemodel.iotype_model import IOTypeStack
    _io_path = _iostack_conf.get('file', 'iolib.json')
    if not os.path.exists(_io_path):
        with open(_io_path, 'w') as io_f_: io_f_.write('{}')
    return IOTypeStack(path=_io_path)


# Initialize the IO type stack
iolib = _build_iotype_stack(_conf.get('iolib', {}))

# Initialize the algorithm stack with entries and IO type stack
entries = []
algorithmlib = AlgorithmStack(
    *entries,
    iolib=iolib
)


def _build_task_queue(_task_queue_conf):
    """
    Builds and returns the task queue based on the configuration.

    Parameters:
    ----------
    _task_queue_conf : dict
        The configuration dictionary for the task queue.

    Returns:
    -------
    TaskQueue
        The initialized task queue instance.
    """
    from .taskmodel.taskqueue import TaskQueue
    return TaskQueue(queue_configs=_task_queue_conf.get('layouts', [{'cuda': 0, 'cpu': 1},
                                                                    {'cuda': 0, 'cpu': os.cpu_count() - 1}]),
                     algorithmlib=algorithmlib)


# Initialize the task queue
taskqueue = _build_task_queue(_conf.get('task_queue', {}))

# Set the server name from configuration or use default
server_name = _conf.get('server_name', 'local_server')


def _config_cache(_cache_config):
    """
    Configures the caching system based on the configuration.

    Parameters:
    ----------
    _cache_config : dict
        The configuration dictionary for the cache.
    
    Raises:
    ------
    TypeError
        If the specified cache type is not supported.
    """
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
    else:
        raise TypeError(f'{_type} Not Supported for Cache.')


# Configure the cache system
_config_cache(_conf.get('cache', {}))
