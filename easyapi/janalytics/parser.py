from .client import ClientEncoder
from .function import FunctionEncoder
from uuid import uuid4

class RecordParser(FunctionEncoder, ClientEncoder):
    
    key = str(uuid4())
    enable_flags = {
        'host': False,
        'parameters': False,
        'signature': False,
    }
    
    @classmethod
    def _fetch_record(cls, flag, func):
        if cls.enable_flags.get(flag, False): return func()
        else: return None
        
    @classmethod
    def record(cls, func, *args, **kwargs):
        _name = cls.get_func_name(func)
        _signature = cls._fetch_record('signature', lambda:cls.signature(*args, **kwargs))
        _host = cls._fetch_record('host', lambda:cls.get_host())
        _parameters = cls._fetch_record('parameters', lambda:cls.get_paramters(*args, **kwargs))
        return dict(
            host = _host,
            signature = _signature,
            name = _name,
            id = cls.key,
            parameters = _parameters
        )
        
    @classmethod
    def set_record_scope(cls, host=None, parameters=None, signature=None):
        if host is not None: cls.enable_flags['host'] = host
        if parameters is not None: cls.enable_flags['parameters'] = parameters
        if signature is not None: cls.enable_flags['signature'] = signature