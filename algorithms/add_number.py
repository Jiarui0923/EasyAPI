id='sum-two-float'
name='Add Two Numbers'
description='Add two float number together and return the result.'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':-1}
io_types = {
    'number': dict(id='number', meta='number', name='float', doc='Universal float', condition=None, version='0.0.1')
}
in_params={
    'a': dict(io_type=io_types['number'], default_value=None, desc='The first number'),
    'b': dict(io_type=io_types['number'], default_value=10, desc='The second number'),
}
out_params={
    'sum': dict(io_type=io_types['number'], default_value=None, desc='The sum of the numbers'),
}

def main(a, b, resources={}):
    cpu_num = resources.get('cpu')
    cuda_num = resources.get('cuda')
    return dict(sum=a+b)
