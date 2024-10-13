from .credentials.auth import JSONAuthenticator
from .iotypemodel.iotype_model import IOTypeStack

authenticator = JSONAuthenticator('credentials.json')
iolib = IOTypeStack(path='iolib.json')