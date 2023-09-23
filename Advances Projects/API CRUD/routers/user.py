from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.schema import Users
from configs.db import session
from middlewares.JWT_bearer import JWTBearer
from models.database import Login

user_router = APIRouter()
    
@user_router.get('/user', tags= ['Logins'], status_code= 200, dependencies= [Depends(JWTBearer())], response_model= list[Users])
def get_users():
    db = session()
    data = jsonable_encoder(db.query(Login).all())
    if len(data) == 0:
        raise HTTPException(status_code= 204)
    return data

@user_router.get('/user/{id}', tags= ['Logins'], status_code= 200, dependencies= [Depends(JWTBearer())], response_model= Users)
def get_user (id : int):
    db = session()
    data = jsonable_encoder(db.query(Login).filter(Login.id == id).one_or_none())
    if data is None:
        raise HTTPException(status_code= 404)
    return data

@user_router.post('/user', tags=['Logins'], status_code= 201, dependencies= [Depends(JWTBearer())], response_model= Users)
def post_user(users : Users):
    db = session()
    new_user = Login(**users.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(content= 'User registered successfully')

@user_router.put('/user/{id}', tags= ['Logins'], status_code= 200, dependencies= [Depends(JWTBearer())], response_model= Users)
def update_user(id : int, users : Users):
    db = session()
    data = db.query(Login).filter(Login.id == id).one_or_none()
    if data is None:
        raise HTTPException(status_code= 404, detail= 'User not found')
    data.name = users.name
    data.email = users.email
    data.password = users.password
    db.commit()
    return JSONResponse(content= 'User modified successfully')

@user_router.delete('/user/{id}', tags= ['Logins'], status_code= 200, dependencies= [Depends(JWTBearer())])
def get_user (id : int):
    db = session()
    data = db.query(Login).filter(Login.id == id).one_or_none()
    if data is None:
        raise HTTPException(status_code= 404, detail= 'User not found')
    db.delete(data)
    db.commit()
    return JSONResponse(content= 'User deleted successfully')