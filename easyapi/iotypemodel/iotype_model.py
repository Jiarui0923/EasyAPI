"""
IOType module
--------------

This module provides classes for managing and manipulating I/O types, including functionality for loading,
saving, and converting data between different formats such as CSV and JSON. It utilizes metadata models to handle
data validation and transformation.

Classes:
--------
IOType
    A class representing an I/O type, including methods for data validation, schema generation, and representation.
IOTypeStack
    A class for managing a collection of I/O types, with methods for loading data from files or dictionaries, 
    and converting data between different formats.

Functions:
----------
None (Class-based module)
"""

import pandas as pd
import json
import os

from .meta_model import IOMetaTypeString
from .meta_model import IOMetaTypeNumber
from .meta_model import IOMetaTypeNumberArray


class IOType(object):
    """
    A class representing an I/O type with metadata validation, schema generation, and data handling.

    Attributes:
    ----------
    meta : str
        The meta type of the data (e.g., 'string', 'number', 'numarray').
    id : str
        A unique identifier for the I/O type.
    name : str
        The name of the I/O type.
    doc : str
        A description of the I/O type.
    condition : any
        A condition that the data must satisfy (default is None).
    version : str
        The version of the I/O type.

    Methods:
    -------
    __repr__()
        Returns a string representation of the IOType instance.
    schema()
        Returns a dictionary schema of the I/O type.
    __call__(data)
        Validates and processes the data according to the meta type and condition.
    """
    
    _accept_meta_types = {
        'string': IOMetaTypeString,
        'number': IOMetaTypeNumber,
        'numarray': IOMetaTypeNumberArray,
    }
    
    def __init__(self, meta='string', id='', name='', doc='', condition=None, version=''):
        """
        Initializes the IOType instance with metadata and validation conditions.

        Parameters:
        ----------
        meta : str, optional
            The meta type for the I/O data (default is 'string').
        id : str, optional
            The unique identifier for the I/O type (default is an empty string).
        name : str, optional
            The name of the I/O type (default is an empty string).
        doc : str, optional
            A description of the I/O type (default is an empty string).
        condition : any, optional
            A condition to validate the data (default is None).
        version : str, optional
            The version of the I/O type (default is an empty string).
        """
        self.meta = meta
        self.id = id
        self.name = name
        self.doc = doc
        self.condition = condition
        self.version = version

    def __repr__(self):
        """
        Returns a string representation of the IOType instance.

        Returns:
        -------
        str
            A string representation of the I/O type.
        """
        return f'<{self.name}({self.meta}) {self.id}:{self.version}>'

    @property
    def schema(self):
        """
        Returns a dictionary schema of the I/O type, containing all metadata.

        Returns:
        -------
        dict
            A dictionary containing the schema of the I/O type.
        """
        return {
            'meta': self.meta,
            'id': self.id,
            'name': self.name,
            'doc': self.doc,
            'condition': self.condition,
            'version': self.version
        }

    def __call__(self, data):
        """
        Validates and processes the data according to the specified meta type and condition.

        Parameters:
        ----------
        data : any
            The data to be validated and processed.

        Returns:
        -------
        any
            The validated and processed data.

        Raises:
        ------
        KeyError
            If the meta type is not found in the accepted meta types.
        """
        _data = self._accept_meta_types[self.meta]
        _data = _data(data, self.condition)
        return _data.data


class IOTypeStack(object):
    """
    A class for managing a collection of I/O types, providing methods for loading and saving I/O types from 
    various data formats (CSV, JSON), and converting data to dictionaries or other formats.

    Attributes:
    ----------
    iotypes : dict
        A dictionary of IOType instances.

    Methods:
    -------
    __setitem__(io_id, io_data)
        Adds or updates an I/O type in the stack.
    __getitem__(io_id)
        Retrieves an I/O type from the stack by ID.
    __len__()
        Returns the number of I/O types in the stack.
    __contains__(io_id)
        Checks if an I/O type exists in the stack.
    _load_dict(dict_)
        Loads I/O types from a dictionary.
    get_records(skip=0, limit=10, full=False)
        Retrieves a list of I/O type records from the stack.
    _load_file(path)
        Loads I/O types from a file (CSV or JSON).
    _load_csv(path)
        Loads I/O types from a CSV file.
    _load_json(path)
        Loads I/O types from a JSON file.
    to_dict(keys=None)
        Converts the stack of I/O types to a dictionary.
    to_csv(path=None)
        Converts the stack of I/O types to a CSV file or string.
    to_json(path=None)
        Converts the stack of I/O types to a JSON string or file.
    """

    def __init__(self, path=None, **kwargs):
        """
        Initializes the IOTypeStack instance with I/O types, either from a file or a dictionary.

        Parameters:
        ----------
        path : str, optional
            The file path to load I/O types from (default is None).
        kwargs : dict, optional
            A dictionary of I/O types to load if no file path is provided.
        """
        self.iotypes = {}
        if path is None:
            self._load_dict(kwargs)
        else:
            self._load_file(path)

    def __setitem__(self, io_id, io_data):
        """
        Adds or updates an I/O type in the stack.

        Parameters:
        ----------
        io_id : str
            The unique identifier for the I/O type.
        io_data : dict
            The data for the I/O type, must include 'id', 'meta', 'name', 'doc', 'version', and 'condition'.

        Raises:
        ------
        SyntaxError
            If the I/O type data is missing required properties.
        """
        _required_properties = ['id', 'meta', 'name', 'doc', 'version', 'condition']
        _filtered_data = {}
        for item in _required_properties:
            if item not in io_data:
                raise SyntaxError(f'Line:{io_id} is irregular')
            _filtered_data[item] = io_data[item]
        self.iotypes[io_id] = IOType(**_filtered_data)

    def __getitem__(self, io_id):
        """
        Retrieves an I/O type from the stack by ID.

        Parameters:
        ----------
        io_id : str
            The unique identifier for the I/O type.

        Returns:
        -------
        IOType
            The IOType instance associated with the given ID.
        """
        return self.iotypes[io_id]

    def __len__(self):
        """
        Returns the number of I/O types in the stack.

        Returns:
        -------
        int
            The number of I/O types in the stack.
        """
        return len(self.iotypes)

    def __contains__(self, io_id):
        """
        Checks if an I/O type exists in the stack.

        Parameters:
        ----------
        io_id : str
            The unique identifier for the I/O type.

        Returns:
        -------
        bool
            True if the I/O type exists in the stack, False otherwise.
        """
        return io_id in self.iotypes

    def _load_dict(self, dict_):
        """
        Loads I/O types from a dictionary.

        Parameters:
        ----------
        dict_ : dict
            A dictionary where the keys are I/O type IDs and the values are the corresponding I/O type data.
        """
        for io_id, io_data in dict_.items():
            self[io_id] = io_data

    def get_records(self, skip=0, limit=10, full=False):
        """
        Retrieves a list of I/O type records from the stack.

        Parameters:
        ----------
        skip : int, optional
            The number of records to skip (default is 0).
        limit : int, optional
            The maximum number of records to retrieve (default is 10).
        full : bool, optional
            Whether to return full record data (default is False).

        Returns:
        -------
        list
            A list of I/O type records.
        """
        if full:
            _keys = list(self.iotypes.items())
        else:
            _keys = list(self.iotypes.keys())
        if limit <= 0:
            return _keys[skip:]
        else:
            return _keys[skip:skip + limit]

    def _load_file(self, path):
        """
        Loads I/O types from a file (CSV or JSON).

        Parameters:
        ----------
        path : str
            The file path to load I/O types from.

        Raises:
        ------
        TypeError
            If the file type is not supported (neither CSV nor JSON).
        """
        if str(path[-3:]).lower() == 'csv':
            self._load_csv(path)
        elif str(path[-4:]).lower() == 'json':
            self._load_json(path)
        else:
            raise TypeError('File type not supported')

    def _load_csv(self, path):
        """
        Loads I/O types from a CSV file.

        Parameters:
        ----------
        path : str
            The file path to the CSV file.
        """
        self._load_dict(pd.read_csv(path).to_dict())

    def _load_json(self, path):
        """
        Loads I/O types from a JSON file.

        Parameters:
        ----------
        path : str
            The file path to the JSON file.
        """
        with open(path, 'r') as f_:
            self._load_dict(json.load(f_))

    def to_dict(self, keys=None):
        """
        Converts the stack of I/O types to a dictionary.

        Parameters:
        ----------
        keys : list of str, optional
            A list of keys to include in the dictionary (default is None, meaning all records will be included).

        Returns:
        -------
        dict
            A dictionary where the keys are I/O type IDs and the values are the corresponding schema of the I/O type.
        """
        if keys is None:
            return {io_id: io_data.schema for io_id, io_data in self.iotypes.items()}
        else:
            return {io_id: self[io_id].schema for io_id in keys}

    def to_csv(self, path=None):
        """
        Converts the stack of I/O types to a CSV file or string.

        Parameters:
        ----------
        path : str, optional
            The path to save the CSV file (default is None, which returns a CSV string).

        Returns:
        -------
        str
            A CSV string if path is None, otherwise saves the CSV to the provided file path.
        """
        if path is None:
            return pd.DataFrame(self.to_dict()).to_csv()
        else:
            pd.DataFrame(self.to_dict()).to_csv(path_or_buf=path)

    def to_json(self, path=None):
        """
        Converts the stack of I/O types to a JSON string or file.

        Parameters:
        ----------
        path : str, optional
            The path to save the JSON file (default is None, which returns a JSON string).

        Returns:
        -------
        str
            A JSON string if path is None, otherwise saves the JSON to the provided file path.
        """
        if path is None:
            return json.dumps(self.to_dict())
        else:
            with open(path, 'w') as f_:
                f_.write(json.dumps(self.to_dict()))
