<img src="/images/tulane_long.png" width="128px"><img src="/images/icon_apl.png" width="256px"><img src="/images/icon_long.png" width="128px"> 

# EasyAPI Algorithm Build Documentation
`Update: 2024-12-13`

This documentation is a guideline about how to tranfer a python function to an EasyAPI endpoint define. In addition, the documentations for related functions and definations are provided here.

## Quickstart
This is an example for define a function for sum of two numbers:
```python
from easyapi import register

@register(required_resources={'cpu':1, 'cuda':0})
def add_two_number(a:float, b:float = 10, resources={}) -> dict[float['sum']]:
    return dict(sum=a+b)
```
To define an EasyAPI endpoint like python function, the given python function should be defined with EasyAPI Types annotated paramters and dictionary like outputs.

To accept the resource assignment from EasyAPI, there must be a parameter called `resources={}`.

The return value of the function should be wrapped with a dictionary with variable name as key. Then, the return defination annotation should follow the same format as actual return value.

This is an example transfer a normal python function to a endpoint function.

This is a normal python function:
```python
def add_two_number(a:float, b:float = 10) -> float:
    return a+b
```
These are steps to transfer it:
1. add resources parameter:
    ```python
    def add_two_number(a:float, b:float = 10, resources={}) -> float:
        return a+b
    ```
2. convert return to be a dictionary
    ```python
    def add_two_number(a:float, b:float = 10, resources={}) -> float:
        return dict(sum = a+b)
    ```
3. convert return type define as dictionary define
    ```python
    def add_two_number(a:float, b:float = 10, resources={}) -> dict[float['sum']]:
        return dict(sum = a+b)
    ```
4. register it with EasyAPI and list required resource
    ```python
    from easyapi import register

    @register(required_resources={'cpu':1, 'cuda':0})
    def add_two_number(a:float, b:float = 10, resources={}) -> dict[float['sum']]:
        return dict(sum = a+b)
    ```

## Type Defination
EasyAPI provide powerful type defination and inference system. Developers could directly use python embeded types including: `float`, `str`, and `list`. It will automatically generate documentation and rich type defination.  

### Types & Meta Types
It also supports advanced defination.  
All EasyAPI types are defined inherented from 3 meta types that could be directly use:
1. number: `Types.Number` for any single number
2. string: `Types.String` for any string
3. numarray: `Types.NumArray` for any list of numbers

The provided types supports documentation and name defination (for returns). The comment will be used to replace the auto-infered documentation for this paramter.  
Documentation define:
```python
Types.Type['comment']
```
Documentation and return key name define:
```python
Types.Type['name', 'comment']
```

As an example, `add_two_number` could also defined as:
```python
from easyapi import register, Types

@register(required_resources={'cpu':1, 'cuda':0})
def add_two_number(a:Types.Number['The first number'],
                   b:Types.Number['The second number'] = 10,
                   resources={}
                   ) -> dict[
                       Types.Number['sum', 'The sum of the two numbers']
                   ]:
    return dict(sum=a+b)
```

### Default Value & Optional Parameters
The default value could be defined just like python function paramter default value as:
```python
Types.Type['comment'] = default_value
```
If default value provided, EasyAPI will consider it as an optional paramter.

### Register
To notice EasyAPI this is an API endpoint, the function needed to be wrapped by `register` decorator.  

```python
register(version='0.0.1', references=None, required_resources=None)
```
- `version`: str = '0.0.1'
    The version of this API endpoint.
- `references`: list[str]|None = None
    The list of references (citations) for this endpoint.
- `required_resources`: dict|None = None
    The required resource for this endpoint. It is a dictionary with two keys: `cpu` and `cuda`, which specified number of cpu cores and cuda devices required separately.

### Result Cache
For some algorithms, they will produce the same result when it got the same inputs and each computation is time-consuming. Therefore, EasyAPI provides an option to cache the output of a given algorithm. It will create a signature with the given paramters and their name as the key. And store the key-value pair in storage system. Once the algorithm receive the same paramter combination, it will search the database to directly get output instead of re-compute it.

```python
cache(disable=False)
```
- `disable`: bool = False
  Disable cache for this function.

### Resources Request
To schedule tasks with different resources requirement, all EasyAPI-endpoint function should accept a parameter named `resources`. It will be a dictionary with keys `cpu` and `cuda`, denoting the devices for this execution.

### Documentation
EasyAPI also allows to define the detail name and documentation for a given endpoint following Python format.

Example:
```python
def endpoint(resources={}):
    """Endpoint Detail Name
    Endpoint Documentation
    """
    return {}
```

### Extended Types
Except the meta types, EasyAPI also provides some rich types and type customization.
#### Rich Types
- `Types.NumberGreaterThan1`: representing a floating-point number greater than 1.
- `Types.PositiveNumber`: representing a floating-point number greater than 0.
- `Types.JSONString`: representing a JSON format string.
#### Customize Type
All EasyAPI type is inherented from `Types.MetaType`. Each type is comprised of `meta`, `id`, `name`, `doc`, `condition`, and `version`. `id` decided the type would be different from other types.  
An example defining a new type.
```python
class CustomizedType(Types.MetaType):
    meta = 'string'
    id = 'customized_type'
    name = 'Customized Type'
    doc = 'This is a customized type'
    condition = None
    version = '0.0.1'
```
- `meta`: defining the meta type could be `string`, `number`, and `numarray`.
- `id`: unique identifier for this type.
- `name`: the name of the endpoint.
- `doc`: the detailed description for this type.
- `condition`: the limitation for this type. for different meta type, the condition format is different.
  - `string`: regular expression
  - `number`: `{'min': min_num, 'max': max_num}`
  - `numarray`: N/A (disabled)
- `version`: version of the endpoint.

A new type could be also inherented from existed type.

As an example:
```python
class ID4Bits(Types.String):
    '''4 bits long unique ID'''
    id = 'id_4_bits'
    name = '4 Bits ID'
    doc = 'This is an unique 4-bits ID'
    condition = '[A-Za-z0-9]{4}'
```