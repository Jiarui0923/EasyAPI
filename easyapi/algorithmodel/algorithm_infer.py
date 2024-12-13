"""
Module: Algorithm Metadata Utilities

Author: Jiarui Li (jli78@tulane.edu)
Institution: Computer Science Department, Tulane University

This module provides utility functions to extract and manage metadata from Python functions, 
with a focus on defining algorithms as modular, annotated units.

Functions:
----------
1. `get_parameters(func)`: Extracts parameter metadata from a function.
2. `get_returns(func)`: Extracts return type metadata from a function.
3. `get_id(func)`: Retrieves the unique identifier (name) of a function.
4. `get_name(func)`: Extracts the name or first line of the docstring of a function.
5. `get_doc(func)`: Extracts the full docstring of a function.
6. `define_algorithm(func, version, references, required_resources)`: Encapsulates function metadata into an algorithm definition.

Dependencies:
-------------
- `inspect`: For analyzing function signatures and annotations.
- `typing`: For handling advanced type annotations.
- `..annotations.meta`: Provides type classes (`MetaType`, `Number`, `NumArray`, `String`).

PEP 8 Compliance:
------------------
This module follows PEP 8 style guidelines.
"""

import inspect
from typing import Annotated, get_args, get_origin

from ..annotations.meta import MetaType, Number, NumArray, String

def get_parameters(func):
    """
    Extracts metadata for the parameters of a given function.

    Parameters:
    -----------
    func : callable
        The function from which to extract parameter metadata.

    Returns:
    --------
    dict
        A dictionary where each key is a parameter name, and the value is a dictionary containing:
        - `io_type`: The type of the parameter (e.g., `Number`, `String`).
        - `desc`: A description of the parameter.
        - `default_value`: The default value of the parameter, if any.

    Raises:
    -------
    TypeError
        If an unsupported annotation type is encountered.
    """
    params = {}
    signature = inspect.signature(func)
    for name, param in signature.parameters.items():
        if name == 'resources':
            continue
        annotation = param.annotation
        if get_origin(annotation) == Annotated:
            io_type, desc = get_args(annotation)
            io_type = io_type.value()
        else:
            if annotation in (float, int):
                io_type, desc = Number.value(), Number.doc
            elif annotation in (str,):
                io_type, desc = String.value(), String.doc
            elif annotation in (list, tuple):
                io_type, desc = NumArray.value(), NumArray.doc
            else:
                raise TypeError(f"Annotation {annotation} is not supported.")
        
        default = param.default if param.default is not inspect._empty else None
        params[name] = {
            'io_type': io_type,
            'desc': desc,
            'default_value': default
        }
    return params

def get_returns(func):
    """
    Extracts metadata for the return values of a given function.

    Parameters:
    -----------
    func : callable
        The function from which to extract return metadata.

    Returns:
    --------
    dict
        A dictionary where each key is a return value name, and the value is a dictionary containing:
        - `io_type`: The type of the return value.
        - `desc`: A description of the return value.
        - `default_value`: Always `None` for return values.

    Raises:
    -------
    TypeError
        If a return annotation lacks a name or exceeds three parameters.
    """
    return_annotations = get_args(inspect.signature(func).return_annotation)
    params = {}
    for annotation in return_annotations:
        annotation = get_args(annotation)
        if len(annotation) == 2:
            io_type, name = annotation
            desc = ''
        elif len(annotation) == 3:
            io_type, name, desc = annotation
        else:
            raise TypeError(f"Return annotation {annotation} must have 2 or 3 elements.")

        if issubclass(io_type, MetaType):
            io_type = io_type.value()
        elif io_type in (float, int):
            io_type = Number.value()
        elif io_type in (str,):
            io_type = String.value()
        elif io_type in (list, tuple):
            io_type = NumArray.value()
        else:
            raise TypeError(f"Return type {io_type} is not supported.")

        params[name] = {
            'io_type': io_type,
            'desc': desc,
            'default_value': None
        }
    return params

def get_id(func):
    """
    Retrieves the unique identifier (name) of a given function.

    Parameters:
    -----------
    func : callable
        The function from which to extract the ID.

    Returns:
    --------
    str
        The name of the function.
    """
    return func.__name__

def get_name(func):
    """
    Retrieves the name or the first line of the docstring of a function.

    Parameters:
    -----------
    func : callable
        The function from which to extract the name.

    Returns:
    --------
    str
        The name of the function or the first line of its docstring.
    """
    doc = inspect.getdoc(func)
    return func.__name__ if doc is None else doc.split('\n')[0]

def get_doc(func):
    """
    Retrieves the full docstring of a given function.

    Parameters:
    -----------
    func : callable
        The function from which to extract the docstring.

    Returns:
    --------
    str
        The full docstring of the function or an empty string if no docstring is provided.
    """
    doc = inspect.getdoc(func)
    return '' if doc is None else '\n'.join(doc.split('\n')[1:])

def define_algorithm(func, version='0.0.1', references=None, required_resources=None):
    """
    Encapsulates function metadata into an algorithm definition.

    Parameters:
    -----------
    func : callable
        The function to define as an algorithm.
    version : str, optional
        The version of the algorithm (default is '0.0.1').
    references : list, optional
        A list of references for the algorithm (default is an empty list).
    required_resources : dict, optional
        A dictionary specifying required resources (default is `{'cpu': -1, 'cuda': -1}`).

    Returns:
    --------
    dict
        A dictionary containing the algorithm metadata, including:
        - `id`: The function's unique identifier.
        - `in_params`: Input parameters metadata.
        - `out_params`: Return values metadata.
        - `name`: The function's name.
        - `description`: The function's docstring.
        - `version`: The algorithm version.
        - `references`: A list of references.
        - `required_resources`: Required resources.
    """
    if references is None:
        references = []
    if required_resources is None:
        required_resources = {'cpu': -1, 'cuda': -1}

    return {
        'func': func,
        'id': get_id(func),
        'in_params': get_parameters(func),
        'out_params': get_returns(func),
        'name': get_name(func),
        'description': get_doc(func),
        'version': version,
        'references': references,
        'required_resources': required_resources
    }
