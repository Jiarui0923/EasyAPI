import warnings
from importlib.util import spec_from_file_location, module_from_spec
from uuid import uuid4
import os
import sys
import logging
import time

from .parameter import Parameter

class Algorithm(object):
    
    def __init__(self, func, id='', in_params={}, out_params={},
                 name='Meta-Algorithm', description='Meta-Algorithm',
                 version='0.0.0', references=[], required_resources={}, iolib=None):
        self.iolib = iolib
        self.id = id
        self.name = name
        self.description = description
        self.version = version
        self.references = references
        self.func = func
        self.required_resources = required_resources
        self.in_params = self.register_params(in_params)
        self.out_params = self.register_params(out_params)
        
    def __repr__(self): return f'<{self.name} {self.id}:{self.version}>'
    
    def _decode_params(self, schema, params):
        _decoded_params = {}
        for io_name, io_type in schema.items():
            if io_name not in params:
                if io_type.optional: _decoded_params[io_name] = io_type.default_value
                else: raise RuntimeError(f'{io_name} not found')
            else: _decoded_params[io_name] = io_type.io_type(params[io_name])
        return _decoded_params
        
    def __call__(self, params, resources={}):
        try:
            _input_params = self._decode_params(params=params, schema=self.in_params)
            _output = self.func(resources=resources, **_input_params)
            _output_params = self._decode_params(params=_output, schema=self.out_params)
            return True, _output_params
        except Exception as e: return False, str(e)
        
    def register_params(self, params={}):
        _params = {}
        for param_name, param in params.items():
            # type_id = param.get('id')
            # if type_id not in self.iolib: self.iolib[type_id] = param
            # else: warnings.warn(f'{type_id} exists, used the previous record.')
            # _params[param_name] = self.iolib[type_id]
            _params[param_name] = Parameter(name=param_name, **param, iolib=self.iolib)
        return _params
    
    @staticmethod
    def load(path, iolib=None):
        _data = Algorithm._load_module_single_file(path)
        if _data is None: return None
        return Algorithm(**_data, iolib=iolib)
    
    @staticmethod
    def _load_module_single_file(path):
        _load_begin = time.perf_counter()
        try:
            spec = spec_from_file_location(name=str(uuid4()), location=path)
            sys.path.append(os.path.abspath(os.path.dirname(path)))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
        except:
            logger = logging.getLogger('uvicorn.warning')
            logger.warning(f'Load {path} failed.')
            return None
        logger = logging.getLogger('uvicorn.info')
        logger.info(f'<ALGORITHM> ({module.id}) {module.name} Loaded [in {time.perf_counter()-_load_begin:.4f}s] from {path}.')
        return {
            'id': module.id,
            'name': module.name,
            'description': module.description,
            'version': module.version,
            'references': module.references,
            'out_params': module.out_params,
            'in_params': module.in_params,
            'required_resources': module.required_resources,
            'func': module.main,
        }
    