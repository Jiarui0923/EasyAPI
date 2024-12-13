"""
Module: Algorithm Framework

This module provides classes and functions for defining, managing, and executing algorithms as modular services.

Classes:
---------
1. Algorithm:
   - Represents an algorithm with metadata, parameters, and execution logic.

2. AlgorithmStack:
   - Manages a collection of algorithms, providing registration and loading capabilities.

Functions:
----------
1. register:
   - Decorator to register a function as an algorithm with versioning and resource requirements.

Dependencies:
-------------
- algorithm: Contains the `Algorithm` class.
- algorithm_infer: Provides `define_algorithm` for defining algorithm metadata.
- logging: Standard Python logging library.
- time: Standard Python time library.
- functools: Provides utilities such as `wraps`.
"""

from .algorithm import Algorithm
from .algorithm_infer import define_algorithm

import logging
import time
from functools import wraps

class AlgorithmStack:
    """
    Manages a collection of algorithms, providing registration, loading, and access capabilities.

    Attributes:
    ----------
    _registered_algorithm : list
        A class-level list to store registered algorithms.
    paths : list
        Paths to algorithm definition files.
    iolib : dict
        Library of input/output types for parameter validation.
    algorithms : dict
        A dictionary of loaded algorithms indexed by their ID.

    Methods:
    -------
    entries:
        Returns a list of registered algorithm IDs.
    register(func, version, references, required_resources):
        Registers a function as an algorithm.
    add(func, version, references, required_resources):
        Adds a function as an algorithm to the stack.
    _load_algorithm(path):
        Loads an algorithm from a file.
    _init_algorithm(algo_dict):
        Initializes an algorithm from a dictionary of attributes.
    """

    _registered_algorithm = []

    def __init__(self, *args, paths=None, iolib=None):
        if paths is None:
            self.paths = args
        else:
            self.paths = paths
        self.iolib = iolib
        _algorithms = [self._load_algorithm(path) for path in self.paths]
        _algorithms += [self._init_algorithm(algo) for algo in self._registered_algorithm]
        _algorithms = [_algorithm for _algorithm in _algorithms if _algorithm is not None]
        self.algorithms = {_algorithm.id: _algorithm for _algorithm in _algorithms}

    def __len__(self):
        return len(self.algorithms)

    def __contains__(self, name):
        return name in self.algorithms

    def __getitem__(self, name):
        return self.algorithms[name]

    def _load_algorithm(self, path):
        """Loads an algorithm from a file path."""
        return Algorithm.load(path, iolib=self.iolib)

    def _init_algorithm(self, algo_dict):
        """Initializes an algorithm from its definition."""
        _load_begin = time.perf_counter()
        try:
            logger = logging.getLogger('uvicorn.info')
            logger.info(f'Load [{time.perf_counter() - _load_begin:.3f}s] > ({algo_dict["id"]}) {algo_dict["name"]}')
            return Algorithm(**algo_dict, iolib=self.iolib)
        except Exception:
            logger = logging.getLogger('uvicorn.warning')
            logger.warning(f'Load [FAILED] > ({algo_dict["id"]}) {algo_dict["name"]}')
            return None

    @property
    def entries(self):
        """Returns a list of algorithm IDs in the stack."""
        return list(self.algorithms.keys())

    @staticmethod
    def register(func, version='0.0.1', references=None, required_resources=None):
        """Registers a function as an algorithm with metadata."""
        if references is None:
            references = []
        if required_resources is None:
            required_resources = {'cpu': -1, 'cuda': -1}
        algo_dict = define_algorithm(func, version=version, references=references, required_resources=required_resources)
        AlgorithmStack._registered_algorithm.append(algo_dict)

    def add(self, func, version='0.0.1', references=None, required_resources=None):
        """Adds a function as an algorithm to the stack."""
        if references is None:
            references = []
        if required_resources is None:
            required_resources = {'cpu': -1, 'cuda': -1}
        algo_dict = define_algorithm(func, version=version, references=references, required_resources=required_resources)
        _algo = self._init_algorithm(algo_dict)
        if _algo is not None:
            self.algorithms[_algo.id] = _algo

def register(version='0.0.1', references=None, required_resources=None):
    """Decorator to register a function as an algorithm."""
    if references is None:
        references = []
    if required_resources is None:
        required_resources = {'cpu': -1, 'cuda': -1}

    def wrap(func):
        AlgorithmStack.register(func, version=version, references=references, required_resources=required_resources)
        return func

    return wrap
