from fastapi import APIRouter
from ..settings import authenticator

route = APIRouter(prefix='/entries')


@route.get('/')
def get_entry_list(auth): pass

@route.post('/{entry_name}')
def submit_task(auth, entry_name): pass

@route.get('/{entry_name}')
def get_entry_doc(auth, entry_name): pass

@route.get('/{entry_name}/name')
def get_entry_name(auth, entry_name): pass

@route.get('/{entry_name}/version')
def get_entry_version(auth, entry_name): pass

@route.get('/{entry_name}/io')
def get_entry_io_schema(auth, entry_name): pass