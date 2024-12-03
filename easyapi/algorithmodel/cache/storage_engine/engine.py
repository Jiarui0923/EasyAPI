class StorageEngine(object):
    
    def __init__(self): self._pool = {}
    def __getitem__(self, key):
        key, query= key
        return self.get(key, query)
    def __setitem__(self, key, value):
        key, query= key
        return self.set(key, query, value)
    def __contains__(self, key):
        key, query= key
        return self.get(key, query) is not None
    def get(self, key, query):
        if key not in self._pool: return None
        else:
            if query not in self._pool[key]: return None
            else: return self._pool[key][query]
    def set(self, key, query, value):
        if key not in self._pool: self._pool[key] = {}
        self._pool[key][query] = value