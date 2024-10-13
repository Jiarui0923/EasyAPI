from fastapi import APIRouter, Depends, HTTPException
from ..settings import authenticator
from ..settings import algorithmlib

route = APIRouter(prefix='/entries')


@route.get('/')
def get_entry_list(skip: int = 0, limit: int = 10,
                   auth_id : str = Depends(authenticator.url_auth)):
    _entries = algorithmlib.entries
    _entries = authenticator.access_check(auth_id, _entries)
    if skip <= 0: skip=0
    if skip > len(_entries): raise HTTPException(status_code=400, detail=f'skip({skip}) is larger than total number ({len(_entries)})')
    if limit <= 0:  return {'total': len(_entries), 'skip': skip, 'limit': None, 'records':_entries[skip:]}
    else: return {'total': len(_entries), 'skip': skip, 'limit': limit, 'records':_entries[skip:skip+limit]}
    

# @route.post('/{entry_name}')
# def submit_task(auth, entry_name): pass

def _get_entry(entry_name):
    if entry_name not in algorithmlib: raise HTTPException(status_code=404, detail=f'{entry_name} not found')
    return algorithmlib[entry_name]
def _check_entry_auth(entry_name, auth_id):
    auth_response = authenticator.access_check(auth_id, [entry_name])
    if len(auth_response) < 0: raise HTTPException(status_code=403)

@route.get('/{entry_name}')
def get_entry_doc(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    response = {
        'id': _entry.id,
        'name': _entry.name,
        'description': _entry.description,
        'version': _entry.version,
        'references': _entry.references,
    }
    return response

@route.get('/{entry_name}/name')
def get_entry_name(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.name

@route.get('/{entry_name}/version')
def get_entry_version(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.version

@route.get('/{entry_name}/desc')
def get_entry_version(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.description

@route.get('/{entry_name}/ref')
def get_entry_version(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    return _entry.references

@route.get('/{entry_name}/in')
def get_entry_in_schema(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    response = {name:param.id for name, param in _entry.in_params.items()}
    return response
    
@route.get('/{entry_name}/out')
def get_entry_out_schema(entry_name, auth_id : str = Depends(authenticator.url_auth)):
    _entry = _get_entry(entry_name)
    _check_entry_auth(entry_name, auth_id)
    response = {name:param.id for name, param in _entry.out_params.items()}
    return response