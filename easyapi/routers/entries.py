"""
FastAPI Routes for Task Submission and Retrieval
------------------------------------------------

This module defines the API routes for managing tasks, including task submission, retrieval of task 
metadata, and handling algorithm entry information. It uses FastAPI for building RESTful services 
and relies on the `authenticator`, `algorithmlib`, and `taskqueue` for task handling and authorization.

Routes:
-------
- GET /entries/: Retrieves a list of algorithm entries.
- POST /entries/{entry_name}: Submits a new task for the specified entry.
- GET /entries/{entry_name}: Retrieves detailed information about an algorithm entry.
- Additional GET routes for retrieving entry metadata such as name, version, description, references, 
  input and output schemas.

Functions:
----------
_get_entry(entry_name)
    Retrieves the entry object for the specified algorithm entry name.

_check_entry_auth(entry_name, auth_id)
    Checks whether the user has authorization to access the specified algorithm entry.

"""

from fastapi import APIRouter, Depends, HTTPException, Request
from ..settings import authenticator
from ..settings import algorithmlib
from ..settings import taskqueue
from ..taskmodel.task import Task
from ..taskmodel.taskholder import task_holder

# Initialize FastAPI router with the 'entries' prefix
route = APIRouter(prefix='/entries', tags=['Algorithm Entries'])

@route.get('/')
async def get_entry_list(skip: int = 0, limit: int = 10, name: bool = False,
                          auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves a list of algorithm entries with optional pagination.
    
    Parameters:
    ----------
    skip : int
        The number of entries to skip (for pagination).
    limit : int
        The maximum number of entries to return (for pagination).
    name : bool
        If true, return only the name of each entry.
    auth_id : str
        The ID of the user making the request, used for authorization.
        
    Returns:
    -------
    dict
        A dictionary containing the total number of entries, skip, limit, and the records (list of entries).
        
    Raises:
    ------
    HTTPException
        If the skip value exceeds the total number of entries, or if other errors occur.
    """
    _entries = algorithmlib.entries
    _entries = authenticator.access_check(auth_id, _entries)
    if name:
        _entries = [(_entry, _get_entry(_entry).name) for _entry in _entries]
    
    if skip <= 0:
        skip = 0
    
    if skip > len(_entries):
        raise HTTPException(status_code=400, detail=f'skip({skip}) is larger than total number ({len(_entries)})')
    
    if limit <= 0:
        return {'total': len(_entries), 'skip': skip, 'limit': None, 'records': _entries[skip:]}
    else:
        return {'total': len(_entries), 'skip': skip, 'limit': limit, 'records': _entries[skip:skip + limit]}

def _get_entry(entry_name):
    """
    Retrieves the algorithm entry by its name.
    
    Parameters:
    ----------
    entry_name : str
        The name of the entry to retrieve.
    
    Returns:
    -------
    object
        The algorithm entry object.
    
    Raises:
    ------
    HTTPException
        If the entry is not found, raises a 404 HTTPException.
    """
    if entry_name not in algorithmlib:
        raise HTTPException(status_code=404, detail=f'{entry_name} not found')
    return algorithmlib[entry_name]

def _check_entry_auth(entry_name, auth_id):
    """
    Checks whether the user has the necessary access rights for the given entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the entry to check.
    auth_id : str
        The ID of the user making the request.
        
    Raises:
    ------
    HTTPException
        If the user is not authorized to access the entry, raises a 403 HTTPException.
    """
    auth_response = authenticator.access_check(auth_id, [entry_name])
    if len(auth_response) < 1:
        raise HTTPException(status_code=403)

@route.post('/{entry_name}')
async def submit_task(entry_name, request: Request,
                      auth_id: str = Depends(authenticator.url_auth)):
    """
    Submits a task for execution on the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry for which to submit a task.
    request : Request
        The request object, used to extract the task parameters.
    auth_id : str
        The ID of the user submitting the task.
    
    Returns:
    -------
    dict
        A dictionary containing the task ID and creation time.
    
    Raises:
    ------
    HTTPException
        If the task parameters cannot be parsed, or if other errors occur.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    
    try:
        _task_params = await request.json()
    except:
        raise HTTPException(status_code=403)
    
    task = Task(access_id=auth_id, algorithm_id=_entry.id,
                input_data=_task_params,
                required_resources=_entry.required_resources)
    task_holder(task_queue=taskqueue, task=task)
    return {'task_id': task.task_id, 'create_time': task.create_time}

@route.get('/{entry_name}')
async def get_entry_doc(entry_name, io: bool = False, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves detailed documentation for an algorithm entry, including inputs and outputs.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    io : bool
        If true, includes input and output parameter details.
    auth_id : str
        The ID of the user requesting the documentation.
    
    Returns:
    -------
    dict
        A dictionary containing the entry details, including inputs and outputs if requested.
    """
    if ',' in entry_name or ';' in entry_name:
        entry_name = str(entry_name).replace(';', ',')
        _entries = {_entry: _get_entry(_entry) for _entry in entry_name.split(',') if len(_entry) > 0}
        for _entry_name in entry_name.split(','):
            if len(_entry_name) > 0:
                _entry = _get_entry(_entry_name)
                _entries[_entry_name] = {
                    'id': _entry.id,
                    'name': _entry.name,
                    'description': _entry.description,
                    'version': _entry.version,
                    'references': _entry.references,
                }
                if io:
                    _entries[_entry_name]['inputs'] = {name: param.property for name, param in _entry.in_params.items()}
                    _entries[_entry_name]['outputs'] = {name: param.property for name, param in _entry.out_params.items()}
        return _entries
    else:
        _entry = _get_entry(entry_name)
        _check_entry_auth(entry_name, auth_id)
        response = {
            'id': _entry.id,
            'name': _entry.name,
            'description': _entry.description,
            'version': _entry.version,
            'references': _entry.references,
        }
        if io:
            response['inputs'] = {name: param.property for name, param in _entry.in_params.items()}
            response['outputs'] = {name: param.property for name, param in _entry.out_params.items()}
        return response

@route.get('/{entry_name}/name')
async def get_entry_name(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the name of the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry name.
    
    Returns:
    -------
    str
        The name of the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.name

@route.get('/{entry_name}/version')
async def get_entry_version(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the version of the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry version.
    
    Returns:
    -------
    str
        The version of the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.version

@route.get('/{entry_name}/desc')
async def get_entry_description(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the description of the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry description.
    
    Returns:
    -------
    str
        The description of the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.description

@route.get('/{entry_name}/ref')
async def get_entry_references(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the references for the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry references.
    
    Returns:
    -------
    str
        The references of the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.references

@route.get('/{entry_name}/in')
async def get_entry_input_schema(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the input schema for the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry input schema.
    
    Returns:
    -------
    dict
        A dictionary of input parameters for the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    response = {name: param.property for name, param in _entry.in_params.items()}
    return response

@route.get('/{entry_name}/out')
async def get_entry_output_schema(entry_name, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the output schema for the specified algorithm entry.
    
    Parameters:
    ----------
    entry_name : str
        The name of the algorithm entry.
    auth_id : str
        The ID of the user requesting the entry output schema.
    
    Returns:
    -------
    dict
        A dictionary of output parameters for the algorithm entry.
    """
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    response = {name: param.property for name, param in _entry.out_params.items()}
    return response
