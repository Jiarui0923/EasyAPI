import requests
import json
from urllib.parse import urljoin

class RecordUploader(object):
    REQUEST_TIMEOUT = 1
    host = 'http://localhost:8001/stat'
    @classmethod
    def post(cls, uri, data):
        try:
            _full_url = urljoin(cls.host, uri)
            requests.post(_full_url, data=json.dumps(data), timeout=cls.REQUEST_TIMEOUT)
        except: pass
    
    @classmethod
    def upload(cls, record):
        cls.post(uri=record.get('name', 'unknown'), data=record)
    
    @classmethod
    def setup_server(cls, host='http://localhost:8001/stat', timeout=1):
        cls.host = host
        cls.REQUEST_TIMEOUT = timeout