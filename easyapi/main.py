"""
Main FastAPI Application for EasyAPI
------------------------------------

This module defines the FastAPI application and includes the main routes for the API. It integrates multiple
routers (iotype, entries, tasks) and provides a root endpoint for basic information about the server. 

The API is secured using the `authenticator` dependency to handle authentication. The root route provides
server information along with the authenticated user's ID.

Routes:
-------
- GET /: A root endpoint that returns the server name and the authenticated user's ID.

Dependencies:
------------
- `authenticator`: Dependency for authenticating users via URL-based authentication.
- `server_name`: A string representing the server's name, imported from the settings.
- `iotype.route`: Router for IO-related operations.
- `entries.route`: Router for entries-related operations.
- `tasks.route`: Router for task-related operations.
"""

from fastapi import FastAPI, Depends
from .settings import authenticator, server_name
from .routers import iotype, entries, tasks

# Initialize the FastAPI app with specific configurations
app = FastAPI(title='EasyAPI', openapi_url=None, docs_url=None, redoc_url=None)

# Include the different routers into the main app
app.include_router(iotype.route)
app.include_router(entries.route)
app.include_router(tasks.route)

@app.get("/")
async def root(auth_id: str = Depends(authenticator.url_auth)):
    """
    Root endpoint that returns the server's name and the authenticated user's ID.
    
    Parameters:
    ----------
    auth_id : str
        The authenticated user's ID, retrieved via URL-based authentication.
        
    Returns:
    -------
    dict
        A dictionary containing the server name and the authenticated user's ID.
    """
    return {'server': server_name, 'id': auth_id}
