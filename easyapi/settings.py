from .credentials.auth import JSONAuthenticator
from .iotypemodel.iotype_model import IOTypeStack
from .algorithmodel.algorithm_stack import AlgorithmStack

authenticator = JSONAuthenticator('credentials.json')
iolib = IOTypeStack(path='iolib.json')
algorithmlib = AlgorithmStack(
    r'C:\Users\11056\Desktop\Research\easyapi\algorithms\add_number.py',
    iolib=iolib
)