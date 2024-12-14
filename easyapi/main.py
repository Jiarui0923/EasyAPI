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
from . import __version__

# Initialize the FastAPI app with specific configurations
_description = """
This project aims to transform a wide range of algorithms—currently implemented as functions, modules, or command-line tools—into accessible services by deploying them through a universal RESTful API server. By adhering to RESTful API standards, the project facilitates easy integration of these algorithms, enabling users to interact with them in a standardized and efficient manner.
The core objective is to develop a flexible API server framework that allows any algorithm to be seamlessly wrapped as a RESTful service. Additionally, we will define a series of data types under a unified protocol to ensure consistency and interoperability across different algorithms and services.
Moreover, the project will introduce an innovative communication protocol that combines elements of existing standards with novel features. This hybrid protocol will allow for delayed response handling, enabling requests to the API to be processed asynchronously and delivering results once they are available.
This approach provides a scalable and user-friendly platform for algorithm deployment and access, streamlining computational tasks across diverse environments.
"""
app = FastAPI(title='EasyAPI',
              description=_description,
              version=__version__,
              openapi_url='/openapi.json',
              docs_url='/docs',
              redoc_url='/redoc')

# Include the different routers into the main app
app.include_router(iotype.route)
app.include_router(entries.route)
app.include_router(tasks.route)

@app.get("/", tags=['Server Information'])
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
