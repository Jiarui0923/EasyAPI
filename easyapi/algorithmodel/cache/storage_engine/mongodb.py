"""
MongoDBStorageEngine module
----------------------------

This module provides the `MongoDBStorageEngine` class that extends the `StorageEngine` 
class for storing and retrieving data from a MongoDB database. It supports basic operations 
like storing and retrieving values using a key-query pair, while interacting with a MongoDB collection.

Classes:
--------
MongoDBStorageEngine
    A class that extends `StorageEngine` to provide MongoDB-based storage functionality.

Functions:
----------
- __init__(host, database): Initializes the MongoDBStorageEngine with the given host and database.
- get(key, query): Retrieves the value associated with the key-query pair from the MongoDB database.
- set(key, query, value): Sets the value for the key-query pair in the MongoDB database.
"""

from .engine import StorageEngine

class MongoDBStorageEngine(StorageEngine):
    """
    A class that extends `StorageEngine` to provide MongoDB-based storage functionality.

    Attributes:
    ----------
    _handle : pymongo.database.Database
        The MongoDB database handle used to interact with collections.

    Methods:
    -------
    __init__(host, database):
        Initializes the MongoDBStorageEngine with the given host and database.
    get(key, query):
        Retrieves the value associated with the key-query pair from the MongoDB database.
    set(key, query, value):
        Sets the value for the key-query pair in the MongoDB database.
    """

    def __init__(self, host='mongodb://localhost', database='easyapi'):
        """
        Initializes the MongoDBStorageEngine with the given host and database.

        Parameters:
        ----------
        host : str, optional
            The MongoDB server URL (default is 'mongodb://localhost').
        database : str, optional
            The name of the MongoDB database (default is 'easyapi').
        """
        from pymongo import MongoClient
        self._handle = MongoClient(host)[database]

    def get(self, key, query):
        """
        Retrieves the value associated with the key-query pair from the MongoDB database.

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
        Sets the value for the key-query pair in the MongoDB database.

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
