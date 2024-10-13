from .algorithm import Algorithm
import os
import warnings


class AlgorithmStack(object):
    
    def __init__(self, *args, paths=[]):
        if len(paths) == 0: self.paths = args
        else: self.paths = paths
        _algorithms = [self._load_algorithm(path) for path in paths]
        self.algorithms = {_algorithm.id:_algorithm for _algorithm in _algorithms}
        
    def __len__(self): return len(self.algorithms)
    
    def _load_algorithm(self, path):
        try: return Algorithm.load(path)
        except: warnings.warn(f'Load module {path} failed')