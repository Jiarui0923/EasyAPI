id='sum-two-float'
name='Add Two Numbers'
description='Add two float number together and return the result.'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':-1}
in_params={
    'a': dict(id='number', meta='number', name='float', doc='Universal float', condition=None, version='0.0.1'),
    'b': dict(id='number', meta='number', name='float', doc='Universal float', condition=None, version='0.0.1'),
}
out_params={
    'sum': dict(id='number', meta='number', name='float', doc='Universal float', condition=None, version='0.0.1'),
}

def main(a, b, resources={}):
    cpu_num = resources.get('cpu')
    cuda_num = resources.get('cuda')
    return dict(sum=a+b)
