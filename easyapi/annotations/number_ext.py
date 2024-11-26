from .meta import Number

class NumberGreaterThan0(Number):
    id   = 'float-greater-than-0'
    name = '0<float'
    doc  = 'Float number > 0'
    condition = {'min':0}
    version   = '0.0.1'