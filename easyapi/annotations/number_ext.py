"""
Module for defining custom number classes with specific conditions.

This module includes two classes: PositiveNumber and NumberGreaterThan1.
Each class inherits from the base class `Number` and defines a specific
condition for the value of the number.

Classes:
    PositiveNumber: Represents a floating-point number greater than 0.
    NumberGreaterThan1: Represents a floating-point number greater than 1.

Author: Jiarui Li
Email: jli78@tulane.edu
"""

from .meta import Number

class PositiveNumber(Number):
    """
    A class representing a floating-point number greater than 0.

    Inherits from the `Number` class and defines a specific condition
    for numbers greater than 0.

    Attributes:
        id (str): Unique identifier for the condition.
        name (str): Name of the condition.
        doc (str): Description of the condition.
        condition (dict): Dictionary containing the minimum value for the condition.
    """
    id = 'float-greater-than-0'
    name = '0<float'
    doc = 'Float number > 0'
    condition = {'min': 0}

class NumberGreaterThan1(Number):
    """
    A class representing a floating-point number greater than 1.

    Inherits from the `Number` class and defines a specific condition
    for numbers greater than 1.

    Attributes:
        id (str): Unique identifier for the condition.
        name (str): Name of the condition.
        doc (str): Description of the condition.
        condition (dict): Dictionary containing the minimum value for the condition.
    """
    id = 'float-greater-than-1'
    name = '1<float'
    doc = 'Float number > 1'
    condition = {'min': 1}
