from fastapi import APIRouter, Depends
from fastapi import HTTPException
from ..settings import authenticator
from ..settings import iolib

route = APIRouter(prefix='/io')

@route.get('/')
async def get_type_list(skip: int = 0, limit: int = 10,
                        auth_id : str = Depends(authenticator.url_auth)):
    if skip <= 0: skip=0
    if skip > len(iolib): raise HTTPException(status_code=400, detail=f'skip({skip}) is larger than total number ({len(iolib)})')
    _keys = iolib.get_records(skip=skip, limit=limit)
    return {'total': len(iolib), 'skip': skip, 'limit':limit, 'records':_keys}

@route.get('/{io_id}')
async def get_type_schema(io_id,
                          auth_id : str = Depends(authenticator.url_auth)):
    if io_id not in iolib: raise HTTPException(status_code=404, detail=f'IO type {io_id} not found')
    _schema = iolib[io_id].schema
    return _schema