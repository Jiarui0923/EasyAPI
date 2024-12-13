"""
AlgorithmCachePool module
--------------------------

This module provides a caching mechanism for algorithm results using a storage engine.
It supports hashing and storing function results based on input parameters for future retrieval.
The cache is implemented using a variety of hash methods, with the ability to switch between them.
The `AlgorithmCachePool` class and the `cache` decorator enable transparent caching for functions.

Classes:
--------
AlgorithmCachePool
    A class responsible for managing the cache of algorithm results.

Functions:
----------
cache(disable=False)
    A decorator function that wraps functions for caching purposes.
"""

from .storage_engine.engine import StorageEngine
import json
import hashlib
from functools import wraps

class AlgorithmCachePool(object):
    """
    A class that manages the caching of algorithm results, using different hash methods 
    and a storage engine to store and retrieve cached values.

    Attributes:
    ----------
    _engine : StorageEngine
        The storage engine used to persist and retrieve cached data.
    _hash_method : str
        The current hashing method used for generating signatures.
    _hash_methods : dict
        A dictionary of available hash methods and their corresponding hash functions.

    Methods:
    -------
    signature(cls, **kwargs)
        Generates a unique signature for the given arguments.
    fetch(cls, func_id, **kwargs)
        Retrieves a cached value from the storage engine using the generated signature.
    record(cls, func_id, value, **kwargs)
        Records a value in the cache using the generated signature.
    cache(cls, disable=False)
        A decorator function for caching the results of a function.
    engine(cls, engine, hash="md5")
        Sets the storage engine and hash method used for caching.
    """
    
    _engine = StorageEngine()
    _hash_method = 'md5'
    _hash_methods = {
        'md5': lambda data: hashlib.md5(data).hexdigest(),
        'sha1': lambda data: hashlib.sha1(data).hexdigest(),
        'sha224': lambda data: hashlib.sha224(data).hexdigest(),
        'sha256': lambda data: hashlib.sha256(data).hexdigest(),
        'sha512': lambda data: hashlib.sha512(data).hexdigest(),
    }
    
    @classmethod
    def signature(cls, **kwargs):
        """
        Generates a unique signature for the given keyword arguments.

        Parameters:
        ----------
        kwargs : dict
            The keyword arguments to be used for generating the signature.

        Returns:
        -------
        str
            The hash signature representing the given arguments.
        """
        _ordered_kwargs = {key: kwargs[key] for key in sorted(kwargs) if key != 'resources'}
        _json = json.dumps(_ordered_kwargs, indent=None)
        _hash = cls._hash_methods[cls._hash_method](_json.encode('utf-8'))
        return _hash
    
    @classmethod
    def fetch(cls, func_id, **kwargs):
        """
        Retrieves a cached value based on the function ID and arguments.

        Parameters:
        ----------
        func_id : str
            The ID of the function to retrieve the cached result for.
        kwargs : dict
            The keyword arguments to generate the signature for.

        Returns:
        -------
        any
            The cached value, or None if not found in the cache.
        """
        _signature = cls.signature(**kwargs)
        _value = cls._engine[(func_id, _signature)]
        return _value
    
    @classmethod
    def record(cls, func_id, value, **kwargs):
        """
        Records a value in the cache for the given function ID and arguments.

        Parameters:
        ----------
        func_id : str
            The ID of the function to cache the result for.
        value : any
            The value to be cached.
        kwargs : dict
            The keyword arguments to generate the signature for.
        """
        _signature = cls.signature(**kwargs)
        cls._engine[(func_id, _signature)] = value
        
    @classmethod
    def cache(cls, disable=False):
        """
        A decorator function for caching the results of a function.

        Parameters:
        ----------
        disable : bool, optional
            Whether to disable caching (default is False).

        Returns:
        -------
        function
            A wrapped function that supports caching.
        """
        def cache_wrapper(func):
            _func_id = func.__name__
            
            @wraps(func)
            def _wrap(**kwargs):
                _value = None
                if not disable:
                    _value = cls.fetch(_func_id, **kwargs)
                if _value is None or disable:
                    _value = func(**kwargs)
                    if not disable:
                        cls.record(_func_id, _value, **kwargs)
                return _value
            
            return _wrap
        
        return cache_wrapper
        
    @classmethod
    def engine(cls, engine, hash="md5"):
        """
        Sets the storage engine and hash method used for caching.

        Parameters:
        ----------
        engine : StorageEngine
            The storage engine to use for caching.
        hash : str, optional
            The hash method to use for generating signatures (default is 'md5').
        """
        cls._hash_method = hash.lower()
        cls._engine = engine

def cache(disable=False):
    """
    A decorator function that wraps functions for caching purposes.

    Parameters:
    ----------
    disable : bool, optional
        Whether to disable caching (default is False).

    Returns:
    -------
    function
        A decorated function with caching functionality.
    """
    return AlgorithmCachePool.cache(disable)
