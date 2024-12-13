from .engine import StorageEngine

class MongoDBStorageEngine(StorageEngine):
    def __init__(self, host='mongodb://localhost', database='easyapi'):
        from pymongo import MongoClient
        self._handle = MongoClient(host)[database]
    def get(self, key, query):
        _data = list(self._handle[key].find({'signature': query}))
        if len(_data) <= 0: return None
        else: return _data[0]['value']
    def set(self, key, query, value):
        if (key, query) not in self: self._handle[key].insert_one({'signature': query, 'value': value})
        else: self._handle[key].update_many({'signature': query}, {'$set': {'value': value}})