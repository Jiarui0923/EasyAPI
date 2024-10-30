from .algorithm import Algorithm
import os
import warnings


class AlgorithmStack(object):
    
    def __init__(self, *args, paths=[], iolib=None):
        if len(paths) == 0: self.paths = args
        else: self.paths = paths
        self.iolib = iolib
        _algorithms = [self._load_algorithm(path) for path in self.paths]
        _algorithms = [_algorithm for _algorithm in _algorithms if _algorithm is not None]
        self.algorithms = {_algorithm.id:_algorithm for _algorithm in _algorithms}
        
    def __len__(self): return len(self.algorithms)
    def __contains__(self, name): return name in self.algorithms
    def __getitem__(self, name): return self.algorithms[name]
    
    def _load_algorithm(self, path):
        try: return Algorithm.load(path, iolib=self.iolib)
        except: warnings.warn(f'Load module {path} failed')
        # return Algorithm.load(path, iolib=self.iolib)
    
    @property
    def entries(self): return list(self.algorithms.keys())