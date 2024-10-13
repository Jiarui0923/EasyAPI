class APIModel(object):
    
    def __init__(self): pass
    
    @staticmethod
    @property
    def input(): return {
        'input_tag': {
            'type': str,
            'description': '...',
            're': '*'
        }
    }
    
    @staticmethod
    @property
    def output(): return {
        'output_tag': {
            'type': str,
            'description': '...',
        }
    }
    
    