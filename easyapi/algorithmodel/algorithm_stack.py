from .algorithm import Algorithm
from .algorithm_infer import define_algorithm
import os
import warnings
import logging
import time


class AlgorithmStack(object):
    _registered_algorithm = []
    def __init__(self, *args, paths=[], iolib=None):
        if len(paths) == 0: self.paths = args
        else: self.paths = paths
        self.iolib = iolib
        _algorithms = [self._load_algorithm(path) for path in self.paths]
        _algorithms += [self._init_algorithm(algo) for algo in self._registered_algorithm]
        _algorithms = [_algorithm for _algorithm in _algorithms if _algorithm is not None]
        self.algorithms = {_algorithm.id:_algorithm for _algorithm in _algorithms}
        
    def __len__(self): return len(self.algorithms)
    def __contains__(self, name): return name in self.algorithms
    def __getitem__(self, name): return self.algorithms[name]
    
    def _load_algorithm(self, path):
        # try: return Algorithm.load(path, iolib=self.iolib)
        # except: warnings.warn(f'Load module {path} failed')
        return Algorithm.load(path, iolib=self.iolib)
    
    def _init_algorithm(self, algo_dict):
        _load_begin = time.perf_counter()
        try:
            logger = logging.getLogger('uvicorn.info')
            logger.info(f'<ALGORITHM> ({algo_dict["id"]}) {algo_dict["name"]} Loaded [in {time.perf_counter()-_load_begin:.4f}s].')
            return Algorithm(**algo_dict, iolib=self.iolib)
        except:
            logger = logging.getLogger('uvicorn.warning')
            logger.warning(f'Load ({algo_dict["id"]}) {algo_dict["name"]} failed.')
            return None
    
    @property
    def entries(self): return list(self.algorithms.keys())
    
    @staticmethod
    def register(func, version='0.0.1', references=[], required_resources={'cpu':-1, 'cuda':-1}):
        algo_dict = define_algorithm(func, version=version, references=references, required_resources=required_resources)
        AlgorithmStack._registered_algorithm.append(algo_dict)
        
    def add(self, func, version='0.0.1', references=[], required_resources={'cpu':-1, 'cuda':-1}):
        algo_dict = define_algorithm(func, version=version, references=references, required_resources=required_resources)
        _algo = self._init_algorithm(algo_dict)
        if _algo is not None: self.algorithms[_algo.id] = _algo
        
def register(version='0.0.1', references=[], required_resources={'cpu':-1, 'cuda':-1}):
    def wrap(func):
        AlgorithmStack.register(func, version=version, references=references, required_resources=required_resources)
        return func
    return wrap
        