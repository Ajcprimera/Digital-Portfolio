from fastapi import  FastAPI
from fastapi.responses import HTMLResponse
from configs.db import engine, base
from middlewares.errors_manager import ErrorManager
from routers.user import user_router
from routers.login_admin import admin_router 

app =  FastAPI()
app.title = "Login users APP"
app.version = "0.0.2"
app.description = "FastAPI login users"
app.add_middleware(ErrorManager)
app.include_router(user_router)
app.include_router(admin_router)

base.metadata.create_all(bind= engine)


@app.get('/', tags= ["home"])
def page():
    return HTMLResponse('<h1 style="font-family:Consent Ny St;color:#B7225E;text-align:center">LOGIN USERS API</h1>')

    
