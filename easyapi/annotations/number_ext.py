from .meta import Number

class PositiveNumber(Number):
    id   = 'float-greater-than-0'
    name = '0<float'
    doc  = 'Float number > 0'
    condition = {'min':0}
    
class NumberGreateThan1(Number):
    id   = 'float-greater-than-1'
    name = '1<float'
    doc  = 'Float number > 1'
    condition = {'min':1}