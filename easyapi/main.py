from fastapi import FastAPI, Depends
from .settings import authenticator
from .routers import iotype

app = FastAPI(title='EasyAPI')

app.include_router(iotype.route)

@app.get("/")
async def root(auth_id : str = Depends(authenticator.url_auth)):
    
    return {'main': 'Hello EasyAPI',
            'id': auth_id}