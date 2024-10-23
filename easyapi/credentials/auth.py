from functools import wraps
from typing import Annotated
from fastapi import Header
from fastapi import HTTPException
from uuid import uuid4
import string
import random
import json

class Authenticator(object):
    
    def __init__(self): self._credentials = {}
    def __len__(self): return len(self._credentials)
    def __setitem__(self, id, pack): self._credentials[id] = {'key':pack.get('key'), 'access':pack.get('key', default=[])}
    def __getitem__(self, id): return self._credentials[id]
    def __delitem__(self, id): del self._credentials[id]
    def __contains__(self, id): return id in self._credentials
    def check(self, id, key):
        if id not in self: return False
        else: return self[id]['key'] == key
    def access_check(self, id, entries):
        if id not in self: return []
        else:
            if self._credentials[id]['access'][0] == '*': return entries
            return [entry for entry in entries
                    if entry in self._credentials[id]['access']]
        
    @staticmethod
    def _random_id(len=12):
        _char_set = string.ascii_letters + string.digits
        _id = random.sample(_char_set, k=len)
        return _id
    
    def create(self, id_len=12, access=[]):
        _id, _key = Authenticator._random_id(len=id_len), str(uuid4())
        self[_id] = {'key':_key, 'access':access}
        return _id, _key
    
    def url_auth(self, easyapi_id: Annotated[str | None, Header()] = '',
                 easyapi_key: Annotated[str | None, Header()] = ''):
        if not self.check(id = easyapi_id, key = easyapi_key): raise HTTPException(status_code=403) 
        else: return easyapi_id
        
        
class JSONAuthenticator(Authenticator):
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self._load_file()
    def _load_file(self):
        with open(self.file_path, 'r') as f_: self._credentials = json.load(f_)
    def _save_file(self):
        with open(self.file_path, 'w') as f_: json.dump(self._credentials, f_)
    def __setitem__(self, id, pack):
        super().__setitem__(id, pack)
        self._save_file()
    def __delitem__(self, id):
        super().__delitem__(id)
        self._save_file()
    def __getitem__(self, id):
        self._load_file()
        return super().__getitem__(id)
        
    
    
    