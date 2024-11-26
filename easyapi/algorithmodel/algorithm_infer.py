import inspect
from typing import Annotated
from typing import get_args
from typing import get_origin

from ..annotations.meta import MetaType
from ..annotations.meta import Number
from ..annotations.meta import NumArray
from ..annotations.meta import String

def get_parameters(func):
    params = {}
    signature = inspect.signature(func)
    for name, param in signature.parameters.items():
        if name == 'resources': continue
        annotation = param.annotation
        if get_origin(annotation) == Annotated:
            io_type, desc = get_args(annotation)
            io_type = io_type.value()
        else:
            if   annotation in (float, int): io_type, desc = Number.value(), Number.doc
            elif annotation in (str, ): io_type, desc = String.value(), String.doc
            elif annotation in (list, tuple): io_type, desc = NumArray.value(), NumArray.doc
            else: raise TypeError(f'{annotation} Not Supported')
        default = param.default
        default = default if default is not inspect._empty else None    
        params[name] = dict(
            io_type = io_type,
            desc = desc,
            default_value = default
        )
    return params

def get_returns(func):
    return_annotations = get_args(inspect.signature(func).return_annotation)
    params = {}
    for annotation in return_annotations:
        annotation = get_args(annotation)
        io_type, name, desc = {}, '', ''
        if len(annotation) <= 1: raise TypeError(f'{annotation} require name')
        elif len(annotation) == 2: (io_type, name) = annotation
        elif len(annotation) == 3: (io_type, name, desc) = annotation
        else: raise TypeError(f'{annotation} should <= 3 parameters')
        
        if issubclass(io_type, MetaType): io_type = io_type.value()
        elif io_type in (float, int): io_type = Number.value()
        elif io_type in (str, ): io_type = String.value()
        elif io_type in (list, tuple): io_type = NumArray.value()
        else: raise TypeError(f'{io_type} Not Supported')
        
        params[name] = dict(
            io_type = io_type,
            desc = desc,
            default_value = None
        )
    return params

def get_id(func): return func.__name__

def get_name(func):
    _doc = inspect.getdoc(func)
    if _doc is None: return func.__name__
    else: return _doc.split('\n')[0]

def get_doc(func):
    _doc = inspect.getdoc(func)
    if _doc is None: return ''
    else: return '\n'.join(_doc.split('\n')[1:])
    
def define_algorithm(func, version='0.0.1', references=[], required_resources={'cpu':-1, 'cuda':-1}):
    return dict(
        func = func,
        id   = get_id(func),
        in_params  = get_parameters(func),
        out_params = get_returns(func),
        name = get_name(func),
        description = get_doc(func),
        version     = version,
        references  = references,
        required_resources = required_resources
    )