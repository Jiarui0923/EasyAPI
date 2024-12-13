"""
Parameter module for wrapping algorithm parameters into a unified format.

This module defines the `Parameter` class to represent an algorithm parameter 
with metadata and default values. It also includes factory methods to create 
parameters of different types, such as string, number, and numerical array.

Author: Jiarui Li
Email: jli78@tulane.edu
Department: Computer Science, Tulane University
"""

from ..iotypemodel.iotype_model import IOType


class Parameter:
    """
    A class to represent an algorithm parameter with metadata and default values.

    Attributes:
    ----------
    name : str
        Name of the parameter.
    io_type : IOType
        The input/output type of the parameter.
    desc : str, optional
        Description of the parameter (default is an empty string).
    default_value : Any, optional
        Default value of the parameter (default is None).
    optional : bool
        Indicates whether the parameter is optional.
    iolib : dict
        A library of IOType objects for parameter reuse.

    Methods:
    -------
    to_dict():
        Converts the parameter to a dictionary representation.
    property:
        Returns the properties of the parameter as a dictionary.
    """

    def __init__(self, name, io_type, desc='', default_value=None, iolib=None):
        """
        Initializes the Parameter class with metadata and default values.

        Parameters:
        ----------
        name : str
            The name of the parameter.
        io_type : IOType
            The input/output type of the parameter.
        desc : str, optional
            Description of the parameter (default is an empty string).
        default_value : Any, optional
            Default value of the parameter (default is None).
        iolib : dict, optional
            A library of IOType objects for parameter reuse (default is None).
        """
        self.name = name
        self.desc = desc
        self.optional = default_value is not None  # If a default value is provided, the parameter is optional
        self.default_value = default_value
        
        type_id = io_type.get('id')

        # Add io_type to iolib if not already present
        if iolib is not None and type_id not in iolib:
            iolib[type_id] = io_type
        
        self.io_type = iolib[type_id] if iolib else io_type

    def __repr__(self):
        """
        Returns a string representation of the Parameter instance.

        Returns:
        -------
        str
            A string representation of the parameter with its name, optional 
            status, and default value.
        """
        return f"< Parameter {self.name}, Optional={self.optional}, Default={self.default_value} >"

    def to_dict(self):
        """
        Converts the parameter instance to a dictionary representation.

        Returns:
        -------
        dict
            A dictionary representing the parameter with its name, type, 
            description, default value, and optional status.
        """
        return {
            'name': self.name,
            'io_type': self.io_type.to_dict(),
            'desc': self.desc,
            'default_value': self.default_value,
            'optional': self.optional
        }

    @property
    def property(self):
        """
        Returns the properties of the parameter as a dictionary.

        Returns:
        -------
        dict
            A dictionary containing the parameter's name, IO type, optional 
            status, default value, and description.
        """
        return {
            'name': self.name,
            'io': self.io_type.id,
            'optional': self.optional,
            'default': self.default_value,
            'desc': self.desc
        }

    @staticmethod
    def string(name, desc='', default_value=None, optional=False):
        """
        Factory method to create a string parameter.

        Parameters:
        ----------
        name : str
            The name of the parameter.
        desc : str, optional
            Description of the parameter (default is an empty string).
        default_value : Any, optional
            Default value of the parameter (default is None).
        optional : bool, optional
            Whether the parameter is optional (default is False).

        Returns:
        -------
        Parameter
            A `Parameter` object with the string IO type.
        """
        return Parameter(
            name, IOType(meta='string', id='string', name='string'),
            desc, default_value, optional
        )

    @staticmethod
    def number(name, desc='', default_value=None, optional=False):
        """
        Factory method to create a number parameter.

        Parameters:
        ----------
        name : str
            The name of the parameter.
        desc : str, optional
            Description of the parameter (default is an empty string).
        default_value : Any, optional
            Default value of the parameter (default is None).
        optional : bool, optional
            Whether the parameter is optional (default is False).

        Returns:
        -------
        Parameter
            A `Parameter` object with the number IO type.
        """
        return Parameter(
            name, IOType(meta='number', id='number', name='number'),
            desc, default_value, optional
        )

    @staticmethod
    def numarray(name, desc='', default_value=None, optional=False):
        """
        Factory method to create a numerical array parameter.

        Parameters:
        ----------
        name : str
            The name of the parameter.
        desc : str, optional
            Description of the parameter (default is an empty string).
        default_value : Any, optional
            Default value of the parameter (default is None).
        optional : bool, optional
            Whether the parameter is optional (default is False).

        Returns:
        -------
        Parameter
            A `Parameter` object with the numerical array IO type.
        """
        return Parameter(
            name, IOType(meta='numarray', id='numarray', name='numarray'),
            desc, default_value, optional
        )


# Predefined meta types for common parameter types
meta_types = {
    'string': IOType(meta='string', id='string', name='string'),
    'number': IOType(meta='number', id='number', name='number'),
    'numarray': IOType(meta='numarray', id='numarray', name='numarray'),
}
