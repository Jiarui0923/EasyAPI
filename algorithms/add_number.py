from easyapi import register, cache, stat, Types

@register(required_resources={'cpu':1, 'cuda':0})
@stat()
@cache(disable=False)
def add_two_number(a:Types.Number['The first number'],
                   b:Types.Number['The second number'] = 10,
                   resources={}
                   ) -> dict[
                       Types.Number['sum', 'The sum of the two numbers']
                   ]:
    """Add Two Numbers
    Add two float number together and return the result.
    """
    cpu_num = resources.get('cpu')
    cuda_num = resources.get('cuda')
    return dict(sum=a+b)
