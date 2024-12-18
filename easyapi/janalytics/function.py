import hashlib
import json

class FunctionEncoder(object):
    MAX_RECORD_STR_LEN = 128
    _hash_method = 'md5'
    _hash_methods = {
        'md5': lambda data: hashlib.md5(data).hexdigest(),
        'sha1': lambda data: hashlib.sha1(data).hexdigest(),
        'sha224': lambda data: hashlib.sha224(data).hexdigest(),
        'sha256': lambda data: hashlib.sha256(data).hexdigest(),
        'sha512': lambda data: hashlib.sha512(data).hexdigest(),
    }
    @classmethod
    def get_func_name(cls, func): return func.__name__
    @classmethod
    def get_paramters(cls, *args, **kwargs):
        _stat_params = {key: kwargs[key] for key in sorted(kwargs)
                        if isinstance(kwargs[key], (float, int)) or
                           (isinstance(kwargs[key], str) and len(kwargs[key]) <= cls.MAX_RECORD_STR_LEN)}
        return json.dumps(_stat_params)
    @classmethod
    def signature(cls, *args, **kwargs):
        _ordered_kwargs = {key: kwargs[key] for key in sorted(kwargs) if key != 'resources'}
        _json = json.dumps(_ordered_kwargs, indent=None)
        _hash = cls._hash_methods[cls._hash_method](_json.encode('utf-8'))
        return _hash
    @classmethod
    def set_hash(cls, hash='MD5'):
        cls._hash_method = hash.lower()
    