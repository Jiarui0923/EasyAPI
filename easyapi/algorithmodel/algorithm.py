from ..settings import iolib
import warnings
from importlib.util import spec_from_file_location, module_from_spec
from uuid import uuid4
import os
import sys

class Algorithm(object):
    
    def __init__(self, func, id='', in_params={}, out_params={},
                 name='Meta-Algorithm', description='Meta-Algorithm',
                 version='0.0.0', references=[], required_resources={}):
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
            if io_name not in params: raise RuntimeError(f'{io_name} not found')
            else: _decoded_params[io_name] = io_type(params[io_name])
        return _decoded_params
        
    def __call__(self, params, resources={}):
        try:
            _input_params = self._decode_params(params=params, schema=self.in_params)
            _output = self.func(resources=resources, **_input_params)
            _output_params = self._decode_params(params=_output, schema=self.out_params)
            return True, _output_params
        except Exception as e: return False, str(e)
        
    def register_params(self, params={}, iolib=iolib):
        _params = {}
        for param_name, param in params.items():
            type_id = param.get('id')
            if type_id not in iolib: iolib[type_id] = param
            else: warnings.warn(f'{type_id} exists, used the previous record.')
            _params[param_name] = iolib[type_id]
        return _params
    
    @staticmethod
    def load(path):
        _data = Algorithm._load_module_single_file(path)
        return Algorithm(**_data)
    
    @staticmethod
    def _load_module_single_file(path):
        spec = spec_from_file_location(name=str(uuid4()), location=path)
        sys.path.append(os.path.abspath(os.path.dirname(path)))
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
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
    