"""
Authenticator module
--------------------

This module defines classes for managing authentication, including storing credentials, checking access,
and creating API keys. It also includes a subclass that supports storing credentials in a JSON file.
The `Authenticator` class provides methods for credential management, and the `JSONAuthenticator` subclass
adds persistent storage using JSON.

Classes:
--------
Authenticator
    A class responsible for managing in-memory authentication credentials and access control.

JSONAuthenticator
    A subclass of Authenticator that stores credentials in a JSON file for persistent storage.

Functions:
----------
None (Class-based module)
"""

from typing import Annotated
from fastapi import Header
from fastapi import HTTPException
from uuid import uuid4
import string
import random
import json

class Authenticator(object):
    """
    A class to manage authentication credentials and access control.

    Attributes:
    ----------
    _credentials : dict
        A dictionary holding user credentials and access control information, where each key is a user ID
        and each value is a dictionary containing 'key' and 'access' lists.

    Methods:
    -------
    __init__(self, credentials={})
        Initializes the authenticator with a set of credentials.

    __len__(self)
        Returns the number of credentials stored.

    __setitem__(self, id, pack)
        Sets the credentials for a given user ID.

    __getitem__(self, id)
        Retrieves the credentials for a given user ID.

    __delitem__(self, id)
        Deletes the credentials for a given user ID.

    __contains__(self, id)
        Checks if the credentials for a given user ID exist.

    check(self, id, key)
        Checks if the provided key matches the stored key for the given user ID.

    access_check(self, id, entries)
        Checks if the given user ID has access to the provided list of entries.

    _random_id(cls, len=12)
        Generates a random ID of the specified length.

    create(self, id_len=12, access=[])
        Creates new credentials (ID and key) and stores them.

    url_auth(self, easyapi_id: Annotated[str | None, Header()] = '', easyapi_key: Annotated[str | None, Header()] = '')
        Authenticates a user based on the provided headers.
    """
    
    def __init__(self, credentials={}):
        """
        Initializes the Authenticator instance with the provided credentials.

        Parameters:
        ----------
        credentials : dict, optional
            A dictionary of credentials to initialize the authenticator with (default is an empty dictionary).
        """
        self._credentials = credentials

    def __len__(self):
        """
        Returns the number of credentials stored.

        Returns:
        -------
        int
            The number of stored credentials.
        """
        return len(self._credentials)

    def __setitem__(self, id, pack):
        """
        Sets the credentials for a given user ID.

        Parameters:
        ----------
        id : str
            The user ID for which to store the credentials.
        pack : dict
            A dictionary containing the 'key' and 'access' lists for the user.
        """
        self._credentials[id] = {'key': pack.get('key'), 'access': pack.get('key', default=[])}

    def __getitem__(self, id):
        """
        Retrieves the credentials for a given user ID.

        Parameters:
        ----------
        id : str
            The user ID for which to retrieve the credentials.

        Returns:
        -------
        dict
            The credentials associated with the user ID.
        """
        return self._credentials[id]

    def __delitem__(self, id):
        """
        Deletes the credentials for a given user ID.

        Parameters:
        ----------
        id : str
            The user ID for which to delete the credentials.
        """
        del self._credentials[id]

    def __contains__(self, id):
        """
        Checks if the credentials for a given user ID exist.

        Parameters:
        ----------
        id : str
            The user ID to check for existence in the credentials store.

        Returns:
        -------
        bool
            True if the user ID exists in the credentials, False otherwise.
        """
        return id in self._credentials

    def check(self, id, key):
        """
        Checks if the provided key matches the stored key for the given user ID.

        Parameters:
        ----------
        id : str
            The user ID to check.
        key : str
            The key to verify against the stored key.

        Returns:
        -------
        bool
            True if the key matches the stored key for the user ID, False otherwise.
        """
        if id not in self:
            return False
        return self[id]['key'] == key

    def access_check(self, id, entries):
        """
        Checks if the given user ID has access to the provided list of entries.

        Parameters:
        ----------
        id : str
            The user ID to check for access.
        entries : list
            A list of entries to check access against.

        Returns:
        -------
        list
            A list of entries the user has access to.
        """
        if id not in self:
            return []
        if self._credentials[id]['access'][0] == '*':
            return entries
        return [entry for entry in entries if entry in self._credentials[id]['access']]

    @staticmethod
    def _random_id(len=12):
        """
        Generates a random ID of the specified length.

        Parameters:
        ----------
        len : int, optional
            The length of the ID to generate (default is 12).

        Returns:
        -------
        list
            A list of randomly selected characters forming the ID.
        """
        _char_set = string.ascii_letters + string.digits
        _id = random.sample(_char_set, k=len)
        return _id

    def create(self, id_len=12, access=[]):
        """
        Creates new credentials (ID and key) and stores them.

        Parameters:
        ----------
        id_len : int, optional
            The length of the ID to generate (default is 12).
        access : list, optional
            A list of access entries for the new credentials (default is an empty list).

        Returns:
        -------
        tuple
            A tuple containing the generated ID and key.
        """
        _id, _key = Authenticator._random_id(len=id_len), str(uuid4())
        self[_id] = {'key': _key, 'access': access}
        return _id, _key

    def url_auth(self, easyapi_id: Annotated[str | None, Header()] = '', easyapi_key: Annotated[str | None, Header()] = ''):
        """
        Authenticates a user based on the provided headers.

        Parameters:
        ----------
        easyapi_id : str, optional
            The user ID provided in the request header.
        easyapi_key : str, optional
            The key provided in the request header.

        Raises:
        ------
        HTTPException
            If the provided ID and key do not match, a 403 HTTP exception is raised.

        Returns:
        -------
        str
            The authenticated user ID.
        """
        if not self.check(id=easyapi_id, key=easyapi_key):
            raise HTTPException(status_code=403)
        return easyapi_id

class JSONAuthenticator(Authenticator):
    """
    A subclass of Authenticator that stores credentials in a JSON file for persistent storage.

    Attributes:
    ----------
    file_path : str
        The path to the JSON file that stores the credentials.

    Methods:
    -------
    __init__(self, file_path)
        Initializes the JSONAuthenticator with the given file path and loads the credentials.
    _load_file(self)
        Loads credentials from the JSON file.
    _save_file(self)
        Saves the current credentials to the JSON file.
    __setitem__(self, id, pack)
        Sets the credentials for a given user ID and saves to the file.
    __delitem__(self, id)
        Deletes the credentials for a given user ID and saves the changes to the file.
    __getitem__(self, id)
        Retrieves the credentials for a given user ID, reloading from the file if necessary.
    """
    
    def __init__(self, file_path):
        """
        Initializes the JSONAuthenticator with the given file path and loads the credentials.

        Parameters:
        ----------
        file_path : str
            The path to the JSON file that stores the credentials.
        """
        super().__init__()
        self.file_path = file_path
        self._load_file()

    def _load_file(self):
        """
        Loads credentials from the JSON file.

        This method reads the credentials from the file and stores them in the _credentials attribute.
        """
        with open(self.file_path, 'r') as f_:
            self._credentials = json.load(f_)

    def _save_file(self):
        """
        Saves the current credentials to the JSON file.

        This method writes the current state of the _credentials attribute to the file.
        """
        with open(self.file_path, 'w') as f_:
            json.dump(self._credentials, f_)

    def __setitem__(self, id, pack):
        """
        Sets the credentials for a given user ID and saves to the file.

        Parameters:
        ----------
        id : str
            The user ID to store.
        pack : dict
            A dictionary containing the 'key' and 'access' lists for the user.
        """
        super().__setitem__(id, pack)
        self._save_file()

    def __delitem__(self, id):
        """
        Deletes the credentials for a given user ID and saves the changes to the file.

        Parameters:
        ----------
        id : str
            The user ID for which to delete the credentials.
        """
        super().__delitem__(id)
        self._save_file()

    def __getitem__(self, id):
        """
        Retrieves the credentials for a given user ID, reloading from the file if necessary.

        Parameters:
        ----------
        id : str
            The user ID for which to retrieve the credentials.

        Returns:
        -------
        dict
            The credentials associated with the user ID.
        """
        self._load_file()
        return super().__getitem__(id)
