import socket

class ClientEncoder(object):
    @classmethod
    def get_host(cls): return socket.gethostname()