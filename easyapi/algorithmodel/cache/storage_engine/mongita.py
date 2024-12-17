"""
MongitaStorageEngine module
----------------------------

This module provides the `MongitaStorageEngine` class that extends the `StorageEngine` 
class for storing and retrieving data from a Mongita database. It supports basic operations 
like storing and retrieving values using a key-query pair, while interacting with a Mongita collection.

Classes:
--------
MongitaStorageEngine
    A class that extends `StorageEngine` to provide Mongita-based storage functionality.

Functions:
----------
- __init__(host, database): Initializes the MongitaStorageEngine with the given host and database.
- get(key, query): Retrieves the value associated with the key-query pair from the Mongita database.
- set(key, query, value): Sets the value for the key-query pair in the Mongita database.
"""

from .engine import StorageEngine
import os

class MongitaStorageEngine(StorageEngine):
    """
    A class that extends `StorageEngine` to provide Mongita-based storage functionality.

    Attributes:
    ----------
    _handle : pymongo.database.Database
        The Mongita database handle used to interact with collections.

    Methods:
    -------
    __init__(host, database):
        Initializes the MongitaStorageEngine with the given host and database.
    get(key, query):
        Retrieves the value associated with the key-query pair from the Mongita database.
    set(key, query, value):
        Sets the value for the key-query pair in the Mongita database.
    """

    def __init__(self, path='.mongita', database='easyapi'):
        """
        Initializes the MongitaStorageEngine with the given host and database.

        Parameters:
        ----------
        path : str, optional
            The path to the database storage folder (default is '.mongita').
        database : str, optional
            The name of the Mongita database (default is 'easyapi').
        """
        from mongita import MongitaClientDisk
        self._handle = MongitaClientDisk(os.path.abspath(path))[database]

    def get(self, key, query):
        """
        Retrieves the value associated with the key-query pair from the Mongita database.

        Parameters:
        ----------
        key : any
            The key for which the value is to be retrieved.
        query : any
            The query to search for in the database.

        Returns:
        -------
        value or None
            The value associated with the key-query pair, or None if not found.
        """
        _data = list(self._handle[key].find({'signature': query}))
        if len(_data) <= 0:
            return None
        else:
            return _data[0]['value']

    def set(self, key, query, value):
        """
        Sets the value for the key-query pair in the Mongita database.

        Parameters:
        ----------
        key : any
            The key for which the value is to be set.
        query : any
            The query for which the value is to be set.
        value : any
            The value to be set for the key-query pair.
        """
        if (key, query) not in self:
            self._handle[key].insert_one({'signature': query, 'value': value})
        else:
            self._handle[key].update_many({'signature': query}, {'$set': {'value': value}})
