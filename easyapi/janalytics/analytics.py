from .parser import RecordParser
from .uploader import RecordUploader

from functools import wraps
import asyncio
import json

class JAnalytics(RecordParser, RecordUploader):
    
    enable = True
    config_path = None

    @classmethod
    def _stat(cls, func, *args, **kwargs):
        if cls.enable:
            try:
                if cls.config_path is not None: cls.load_config_()
                _record = cls.record(func, *args, **kwargs)
                cls.upload(_record)
            except: pass
    
    @classmethod
    def stat(cls):
        def stat_wrapper(func):
            @wraps(func)
            def _wrap(*args, **kwargs):
                cls._stat(func, *args, **kwargs)
                return func(*args, **kwargs)
            return _wrap
        return stat_wrapper
    
    @classmethod
    def config(cls, enable=True, host='http://localhost:8001/stat', timeout=1, hash='MD5',
               record_host=False, record_signature=False, record_parameters=False):
        cls.set_record_scope(host=record_host, signature=record_signature, parameters=record_parameters)
        cls.set_hash(hash=hash)
        cls.enable = enable
        cls.setup_server(host=host, timeout=timeout)
        
    @classmethod
    def load_config(cls, path):
        cls.config_path = path
    
    @classmethod
    def load_config_(cls):
        with open(cls.config_path, 'r') as _f_config:
            config = json.load(_f_config)
            cls.config(enable=config.get('enable', True),
                       host=config.get('host', 'http://localhost:8001/stat'),
                       timeout=config.get('timeout', 1),
                       record_host=config.get('record_host', False),
                       record_parameters=config.get('record_parameter', False),
                       record_signature=config.get('record_signature', False),)
            
def stat(): return JAnalytics.stat()