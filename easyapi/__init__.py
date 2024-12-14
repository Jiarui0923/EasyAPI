"""
Module: Initialization for Algorithm Framework

This module initializes the algorithm framework by importing necessary components
and making them available for use. It imports algorithms, cache management, and the 
main application instance.

Dependencies:
-------------
- annotations: Provides type annotations for various components.
- algorithm_stack: Contains the `register` decorator for registering algorithms.
- cache: Provides cache management functionality.
- main: Contains the main FastAPI application instance (`app`).

Functions:
----------
This module does not define any new functions but imports necessary components
to initialize and configure the application.
"""

__version__ = '1.0.0'

from . import annotations as Types
from .algorithmodel.algorithm_stack import register
from .algorithmodel.cache import cache
from .main import app
