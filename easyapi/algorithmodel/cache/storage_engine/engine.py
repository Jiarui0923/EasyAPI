"""
StorageEngine module
--------------------

This module provides the `StorageEngine` class that allows storing, retrieving, 
and checking values based on key-query pairs. It supports basic dictionary-like 
operations and is designed to manage data in a nested dictionary format.

Classes:
--------
StorageEngine
    A class to manage key-query-value pairs with methods for storing, 
    retrieving, and checking values.

Functions:
----------
- __getitem__(key): Retrieves the value associated with the key-query pair.
- __setitem__(key, value): Sets the value for the key-query pair.
- __contains__(key): Checks if the key-query pair exists in the storage.
- get(key, query): Retrieves the value for a given key-query pair, or None if not found.
- set(key, query, value): Sets the value for the key-query pair in the storage.
"""

class StorageEngine(object):
    """
    A class to represent a simple storage engine that supports storing, 
    retrieving, and checking items based on a key-query pair.

    Attributes:
    ----------
    _pool : dict
        A dictionary that stores the data, where the key maps to another 
        dictionary, which maps a query to a value.

    Methods:
    -------
    __getitem__(key):
        Retrieves the value associated with the key-query pair.
    __setitem__(key, value):
        Sets the value for the key-query pair.
    __contains__(key):
        Checks if the key-query pair exists in the storage.
    get(key, query):
        Retrieves the value for a given key-query pair, or None if not found.
    set(key, query, value):
        Sets the value for the key-query pair in the storage.
    """

    def __init__(self):
        """
        Initializes the StorageEngine instance with an empty pool.

        Attributes:
        ----------
        _pool : dict
            A dictionary to store key-query-value pairs.
        """
        self._pool = {}

    def __getitem__(self, key):
        """
        Retrieves the value associated with the key-query pair.

        Parameters:
        ----------
        key : tuple
            A tuple consisting of the key and the query.

        Returns:
        -------
        value or None
            The value associated with the key-query pair, or None if not found.
        """
        key, query = key
        return self.get(key, query)

    def __setitem__(self, key, value):
        """
        Sets the value for the key-query pair.

        Parameters:
        ----------
        key : tuple
            A tuple consisting of the key and the query.
        value : any
            The value to be set for the key-query pair.
        """
        key, query = key
        return self.set(key, query, value)

    def __contains__(self, key):
        """
        Checks if the key-query pair exists in the storage.

        Parameters:
        ----------
        key : tuple
            A tuple consisting of the key and the query.

        Returns:
        -------
        bool
            True if the key-query pair exists, False otherwise.
        """
        key, query = key
        return self.get(key, query) is not None

    def get(self, key, query):
        """
        Retrieves the value for a given key-query pair.

        Parameters:
        ----------
        key : any
            The key for which the value is to be retrieved.
        query : any
            The query for which the value is to be retrieved.

        Returns:
        -------
        value or None
            The value associated with the key-query pair, or None if not found.
        """
        if key not in self._pool:
            return None
        else:
            if query not in self._pool[key]:
                return None
            else:
                return self._pool[key][query]

    def set(self, key, query, value):
        """
        Sets the value for the key-query pair in the storage.

        Parameters:
        ----------
        key : any
            The key for which the value is to be set.
        query : any
            The query for which the value is to be set.
        value : any
            The value to be set for the key-query pair.
        """
        if key not in self._pool:
            self._pool[key] = {}
        self._pool[key][query] = value
