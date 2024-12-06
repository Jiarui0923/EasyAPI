from .storage_engine.engine import StorageEngine
import json
import hashlib
from functools import wraps

class AlgorithmCachePool(object):
    
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
        _ordered_kwargs = {key:kwargs[key] for key in sorted(kwargs)}
        _json = json.dumps(_ordered_kwargs, indent=None)
        _hash = cls._hash_methods[cls._hash_method](_json.encode('utf-8'))
        return _hash
    
    @classmethod
    def fetch(cls, func_id, **kwargs):
        _signature = cls.signature(**kwargs)
        _value = cls._engine[(func_id, _signature)]
        return _value
    
    @classmethod
    def record(cls, func_id, value, **kwargs):
        _signature = cls.signature(**kwargs)
        cls._engine[(func_id, _signature)] = value
        
    @classmethod
    def cache(cls, disable=False):
        def cache_wrapper(func):
            _func_id = func.__name__
            @wraps(func)
            def _wrap(**kwargs):
                _value = None
                if not disable: _value = cls.fetch(_func_id, **kwargs)
                if _value is None or disable:
                    _value = func(**kwargs)
                    if not disable: cls.record(_func_id, _value, **kwargs)
                return _value
            return _wrap
        return cache_wrapper
        
    @classmethod
    def engine(cls, engine, hash="md5"):
        cls._hash_method = hash.lower()
        cls._engine = engine
        
def cache(disable=False):
    return AlgorithmCachePool.cache(disable)