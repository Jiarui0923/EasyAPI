

class Parameter(object):
    
    def __init__(self, name, io_type, desc='', default_value=None, iolib=None):
        self.name = name
        self.desc = desc
        self.optional = False if default_value is None else True
        self.default_value = default_value
        type_id = io_type.get('id')
        if type_id not in iolib: iolib[type_id] = io_type
        self.io_type = iolib[type_id]
    
    @property
    def property(self):
        return {
            'name': self.name,
            'io': self.io_type.id,
            'optional': self.optional,
            'default': self.default_value,
            'desc': self.desc
        }
    