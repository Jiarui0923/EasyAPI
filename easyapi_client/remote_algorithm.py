from .iotypemodel.iotype_model import IOType
from .progress import LoadProgress
from . import docflow as doc

import time


class RemoteAlgorithm(object):
    
    def __init__(self, client, entry_name):
        
        self._client = client
        self._entry_name = entry_name
        self._io_lib = {}
        
        self._load_algo_info()
        self._load_in_out_params()
        self._doc = self._build_doc()
        self.__doc__ = self._doc
        
    def __repr__(self): return self._doc
    def _repr_markdown_(self): return self._doc
        
    def _load_algo_info(self):
        _algo_info = self._client._get_entry(self._entry_name)
        self.id = _algo_info.get('id')
        self.name = _algo_info.get('name')
        self.description = _algo_info.get('description')
        self.version = _algo_info.get('version')
        self.references = _algo_info.get('references')
        
    def _load_io_info(self, io_name):
        if io_name not in self._io_lib:
            self._io_lib[io_name] = IOType(**self._client._get_io(io_name))
        return self._io_lib[io_name]
    
    def _load_in_out_params(self):
        self.inputs = {param:self._load_io_info(io_name)
                       for param, io_name
                       in self._client._get_entry_input(self._entry_name).items()}
        self.outputs = {param:self._load_io_info(io_name)
                        for param, io_name
                        in self._client._get_entry_output(self._entry_name).items()}
    
    def _build_doc(self):
        _doc = doc.Document(
            doc.Title(self.name, level=3),
            doc.Text(f'\n`{self.version}`  \n{self.description}  \n'),
            doc.Title('Parameters', level=4),
            doc.Sequence({param:f'`{iotype.meta}` ({iotype.name}) {iotype.doc}'
                          for param, iotype
                          in self.inputs.items()}),
            doc.Title('Returns', level=4),
            doc.Sequence({param:f'`{iotype.meta}` ({iotype.name}) {iotype.doc}'
                          for param, iotype
                          in self.outputs.items()}),
            doc.Title('References', level=4),
            doc.Sequence(self.references),
        )
        return _doc.markdown
        
    def __call__(self, **kwargs):
        _params = {}
        for arg_name, arg_regular in self.inputs.items():
            if arg_name not in kwargs: raise RuntimeError(f'{arg_name} Required.')
            else:
                _params[arg_name] = arg_regular(kwargs[arg_name])
        _task_id = self._client._submit_task(entry_name = self._entry_name, params = _params)
        _task_progress_bar = LoadProgress('Task Submitted', timer=True)
        time.sleep(0.1)
        _response = self._client._get_task_return(_task_id)
        while 'success' not in _response:
            _task_progress_bar.update(_response.get('status'))
            time.sleep(0.1)
            _response = self._client._get_task_return(_task_id)
        if not _response['success']:
            _task_progress_bar.error(_response.get('output'))
            raise RuntimeError(_response.get('output'))
        else:
            _task_progress_bar.done('Task Finished, output is ready.')
            return _response.get('output')