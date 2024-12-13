"""
Algorithm module for wrapping a Python function as an algorithm portal.

This module defines the `Algorithm` class, which allows for the definition
and execution of an algorithm along with metadata, input/output parameters, 
and required resources.

Author: Jiarui Li
Email: jli78@tulane.edu
Department: Computer Science, Tulane University

PEP 8 Compliance:
------------------
This module follows PEP 8 style guidelines.
"""

import os
import sys
import logging
import time
from importlib.util import spec_from_file_location, module_from_spec
from uuid import uuid4

from .parameter import Parameter


class Algorithm:
    """
    A class to represent an algorithm with metadata, parameters, and execution logic.

    Attributes:
    ----------
    func : callable
        The function implementing the algorithm.
    id : str
        Identifier for the algorithm.
    in_params : dict
        Input parameters for the algorithm.
    out_params : dict
        Output parameters for the algorithm.
    name : str
        Name of the algorithm.
    description : str
        Description of the algorithm.
    version : str
        Version of the algorithm.
    references : list
        References associated with the algorithm.
    required_resources : dict
        Resources required by the algorithm.
    iolib : dict
        Library of input/output types.

    Methods:
    -------
    __call__(params, resources={}):
        Executes the algorithm with the provided parameters and resources.
    register_params(params):
        Registers input or output parameters.
    load(path, iolib=None):
        Loads an algorithm definition from a file.
    """

    def __init__(self, func, id='', in_params=None, out_params=None,
                 name='Meta-Algorithm', description='Meta-Algorithm',
                 version='0.0.0', references=None, required_resources=None, iolib=None):
        """
        Initializes the Algorithm class with metadata, parameters, and function.

        Parameters:
        ----------
        func : callable
            The function implementing the algorithm.
        id : str, optional
            Identifier for the algorithm (default is '').
        in_params : dict, optional
            Input parameters for the algorithm (default is None).
        out_params : dict, optional
            Output parameters for the algorithm (default is None).
        name : str, optional
            Name of the algorithm (default is 'Meta-Algorithm').
        description : str, optional
            Description of the algorithm (default is 'Meta-Algorithm').
        version : str, optional
            Version of the algorithm (default is '0.0.0').
        references : list, optional
            References associated with the algorithm (default is None).
        required_resources : dict, optional
            Resources required by the algorithm (default is None).
        iolib : dict, optional
            Library of input/output types (default is None).
        """
        self.iolib = iolib
        self.id = id
        self.name = name
        self.description = description
        self.version = version
        self.references = references if references is not None else []
        self.func = func
        self.required_resources = required_resources if required_resources is not None else {}
        self.in_params = self.register_params(in_params or {})
        self.out_params = self.register_params(out_params or {})

    def __repr__(self):
        """
        Returns a string representation of the Algorithm object.

        Returns:
        -------
        str
            A string representing the algorithm, including name, id, and version.
        """
        return f"<{self.name} {self.id}:{self.version}>"

    def _decode_params(self, schema, params):
        """
        Decodes and validates input or output parameters against the schema.

        Parameters:
        ----------
        schema : dict
            The parameter schema (input or output).
        params : dict
            The parameters to decode.

        Returns:
        -------
        dict
            A dictionary of decoded parameters.
        """
        _decoded_params = {}
        for io_name, io_type in schema.items():
            if io_name not in params:
                if io_type.optional:
                    _decoded_params[io_name] = io_type.default_value
                else:
                    raise RuntimeError(f'{io_name} not found')
            else:
                _decoded_params[io_name] = io_type.io_type(params[io_name])
        return _decoded_params

    def __call__(self, params, resources=None):
        """
        Executes the algorithm with the provided parameters and resources.

        Parameters:
        ----------
        params : dict
            A dictionary of input parameters for the algorithm.
        resources : dict, optional
            Resources required for the execution (default is None).

        Returns:
        -------
        tuple
            A tuple (success, output), where success is a boolean indicating
            if the execution was successful, and output contains either the 
            decoded output parameters or an error message.
        """
        resources = resources if resources is not None else {}
        try:
            _input_params = self._decode_params(params=params, schema=self.in_params)
            _output = self.func(resources=resources, **_input_params)
            _output_params = self._decode_params(params=_output, schema=self.out_params)
            return True, _output_params
        except Exception as e:
            return False, str(e)

    def register_params(self, params=None):
        """
        Registers input or output parameters for the algorithm.

        Parameters:
        ----------
        params : dict, optional
            A dictionary of parameters (default is None).

        Returns:
        -------
        dict
            A dictionary of registered parameters.
        """
        _params = {}
        for param_name, param in (params or {}).items():
            _params[param_name] = Parameter(name=param_name, **param, iolib=self.iolib)
        return _params

    @staticmethod
    def load(path, iolib=None):
        """
        Loads an algorithm definition from a file.

        Parameters:
        ----------
        path : str
            Path to the Python file containing the algorithm definition.
        iolib : dict, optional
            Library of input/output types (default is None).

        Returns:
        -------
        Algorithm or None
            An Algorithm object if loading is successful, otherwise None.
        """
        _data = Algorithm._load_module_single_file(path)
        if _data is None:
            return None
        return Algorithm(**_data, iolib=iolib)

    @staticmethod
    def _load_module_single_file(path):
        """
        Loads a Python module from a single file and extracts algorithm metadata.

        Parameters:
        ----------
        path : str
            Path to the Python file containing the algorithm definition.

        Returns:
        -------
        dict or None
            A dictionary containing the algorithm's metadata if successful, 
            otherwise None.
        """
        _load_begin = time.perf_counter()
        try:
            spec = spec_from_file_location(name=str(uuid4()), location=path)
            sys.path.append(os.path.abspath(os.path.dirname(path)))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception:
            logger = logging.getLogger('uvicorn.warning')
            logger.warning(f'Load {path} failed.')
            return None

        logger = logging.getLogger('uvicorn.info')
        logger.info(f'<ALGORITHM> ({module.id}) {module.name} Loaded [in {time.perf_counter() - _load_begin:.4f}s] from {path}.')
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
