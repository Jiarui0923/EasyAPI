from typing import Annotated

class MetaType(object):
    meta = ''
    id   = ''
    name = ''
    doc  = ''
    condition = None
    version   = '0.0.1'
    @classmethod
    def value(cls): return dict(meta=cls.meta,
                                id=cls.id,
                                name=cls.name,
                                doc=cls.doc,
                                condition=cls.condition,
                                version=cls.version)
    def __class_getitem__(cls, params):
        if not isinstance(params, tuple):
            params = (params,)
        return Annotated[cls, *params]
    
class Number(MetaType):
    meta = 'number'
    id   = 'number'
    name = 'float'
    doc  = 'Universal float'
    condition = None
    version   = '0.0.1'

class String(MetaType):
    meta = 'string'
    id   = 'string'
    name = 'string'
    doc  = 'Universal string'
    condition = None
    version   = '0.0.1'

class NumArray(MetaType):
    meta = 'numarray'
    id   = 'numarray'
    name = 'array[float]'
    doc  = 'Float array'
    condition = None
    version   = '0.0.1'
    