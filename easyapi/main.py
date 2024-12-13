from fastapi   import FastAPI
from fastapi   import Depends

from .settings import authenticator
from .settings import server_name
from .routers  import iotype
from .routers  import entries
from .routers  import tasks

app = FastAPI(title='EasyAPI', openapi_url=None, docs_url=None, redoc_url=None)

app.include_router(iotype.route)
app.include_router(entries.route)
app.include_router(tasks.route)

@app.get("/")
async def root(auth_id : str = Depends(authenticator.url_auth)):
    
    return {'server': server_name,
            'id': auth_id}