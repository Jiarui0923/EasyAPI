"""
FastAPI Routes for I/O Type Retrieval
--------------------------------------

This module defines the API routes for retrieving I/O type information. It provides endpoints for listing 
available I/O types, retrieving specific I/O type schemas, and handling pagination. The routes are secured 
with user authentication via the `authenticator` dependency and use the `iolib` for I/O type management.

Routes:
-------
- GET /io/: Retrieves a paginated list of available I/O types.
- GET /io/{io_id}: Retrieves the schema for a specific I/O type.

Functions:
----------
get_type_list(skip, limit, full, auth_id)
    Retrieves a paginated list of I/O types.
    
get_type_schema(io_id, auth_id)
    Retrieves the schema for a specific I/O type by its ID.

"""

from fastapi import APIRouter, Depends, HTTPException
from ..settings import authenticator
from ..settings import iolib

# Initialize FastAPI router with the 'io' prefix
route = APIRouter(prefix='/io')

@route.get('/')
async def get_type_list(skip: int = 0, limit: int = 10, full: bool = False,
                        auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves a paginated list of I/O types, with optional full details.
    
    Parameters:
    ----------
    skip : int
        The number of entries to skip (for pagination).
    limit : int
        The maximum number of entries to return (for pagination).
    full : bool
        If true, return full details of the I/O types.
    auth_id : str
        The ID of the user making the request, used for authorization.
        
    Returns:
    -------
    dict
        A dictionary containing the total number of I/O types, skip, limit, and the records (list of I/O types).
        
    Raises:
    ------
    HTTPException
        If the skip value exceeds the total number of I/O types.
    """
    if skip <= 0:
        skip = 0
    
    if skip > len(iolib):
        raise HTTPException(status_code=400, detail=f'skip({skip}) is larger than total number ({len(iolib)})')
    
    if full:
        _keys = dict(iolib.get_records(skip=skip, limit=limit, full=True))
    else:
        _keys = iolib.get_records(skip=skip, limit=limit)
    
    return {'total': len(iolib), 'skip': skip, 'limit': limit, 'records': _keys}

@route.get('/{io_id}')
async def get_type_schema(io_id, auth_id: str = Depends(authenticator.url_auth)):
    """
    Retrieves the schema for a specific I/O type by its ID.
    
    Parameters:
    ----------
    io_id : str
        The ID of the I/O type to retrieve the schema for.
    auth_id : str
        The ID of the user making the request, used for authorization.
    
    Returns:
    -------
    dict
        The schema of the requested I/O type.
    
    Raises:
    ------
    HTTPException
        If the I/O type with the specified ID is not found.
    """
    if io_id not in iolib:
        raise HTTPException(status_code=404, detail=f'IO type {io_id} not found')
    
    _schema = iolib[io_id].schema
    return _schema
