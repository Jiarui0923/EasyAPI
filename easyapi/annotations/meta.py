"""
Module: MetaType and Derived Classes

Author: Jiarui Li (jli78@tulane.edu)
Institution: Computer Science Department, Tulane University

This module defines the `MetaType` base class and its derived types (`Number`, `String`, `NumArray`).
These classes provide metadata representation for various types, such as numbers, strings, and numeric arrays,
and can be used in type annotations for enhanced type safety and documentation.

Classes:
--------
1. `MetaType`: Base class for metadata representations.
2. `Number`: Represents numerical types.
3. `String`: Represents string types.
4. `NumArray`: Represents arrays of numerical types.

PEP 8 Compliance:
------------------
This module follows PEP 8 style guidelines.
"""

from typing import Annotated

class MetaType:
    """
    Base class for metadata representation.

    Attributes:
    -----------
    meta : str
        Metadata type identifier.
    id : str
        Unique identifier for the type.
    name : str
        Human-readable name for the type.
    doc : str
        Documentation or description of the type.
    condition : Any
        Optional condition associated with the type.
    version : str
        Version of the metadata type.
    
    Methods:
    --------
    value():
        Returns a dictionary representation of the metadata type.

    __class_getitem__(cls, params):
        Enables the use of `Annotated` with the type.
    """

    meta = ''
    id = ''
    name = ''
    doc = ''
    condition = None
    version = '0.0.1'

    @classmethod
    def value(cls):
        """
        Returns a dictionary representation of the metadata type.

        Returns:
        --------
        dict
            A dictionary containing metadata attributes.
        """
        return {
            'meta': cls.meta,
            'id': cls.id,
            'name': cls.name,
            'doc': cls.doc,
            'condition': cls.condition,
            'version': cls.version
        }

    def __class_getitem__(cls, params):
        """
        Enables the use of `Annotated` with the type.

        Parameters:
        -----------
        params : Any
            Parameters to be included in the annotation.

        Returns:
        --------
        Annotated
            Annotated type with the specified parameters.
        """
        if not isinstance(params, tuple):
            params = (params,)
        return Annotated[cls, *params]

class Number(MetaType):
    """
    Represents numerical types.

    Attributes:
    -----------
    meta : str
        Metadata type identifier ('number').
    id : str
        Unique identifier ('number').
    name : str
        Human-readable name ('float').
    doc : str
        Documentation ('Universal float').
    condition : Any
        Optional condition (None).
    version : str
        Version of the metadata type ('0.0.1').
    """

    meta = 'number'
    id = 'number'
    name = 'float'
    doc = 'Universal float'
    condition = None
    version = '0.0.1'

class String(MetaType):
    """
    Represents string types.

    Attributes:
    -----------
    meta : str
        Metadata type identifier ('string').
    id : str
        Unique identifier ('string').
    name : str
        Human-readable name ('string').
    doc : str
        Documentation ('Universal string').
    condition : Any
        Optional condition (None).
    version : str
        Version of the metadata type ('0.0.1').
    """

    meta = 'string'
    id = 'string'
    name = 'string'
    doc = 'Universal string'
    condition = None
    version = '0.0.1'

class NumArray(MetaType):
    """
    Represents arrays of numerical types.

    Attributes:
    -----------
    meta : str
        Metadata type identifier ('numarray').
    id : str
        Unique identifier ('numarray').
    name : str
        Human-readable name ('array[float]').
    doc : str
        Documentation ('Float array').
    condition : Any
        Optional condition (None).
    version : str
        Version of the metadata type ('0.0.1').
    """

    meta = 'numarray'
    id = 'numarray'
    name = 'array[float]'
    doc = 'Float array'
    condition = None
    version = '0.0.1' 
