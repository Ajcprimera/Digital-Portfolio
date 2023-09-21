from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from uuid import uuid4
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field
from JWT_manager import create_token, validate_token
from read_file import read_file, write_file
from typing import Optional

app =  FastAPI()
app.title = "Whatsapp data contact APP"
app.version = "0.0.1"
app.description = "FastAPI whatsapp contact"
data = read_file()

class Contacts(BaseModel):
    id: Optional[str] = None
    name : str = Field(min_length=4, max_length = 20)
    number : str = Field(min_length=8, max_length = 20)
    
    model_config ={
        "json_schema_extra": {
            "examples": [
                {
                    "name": "My name",
                    "number": "Whatsapp number",
                }
            ]
        }}
    
class UserAdmin(BaseModel):
    email: str
    password: str

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request): 
        auth =  await super().__call__(request) 
        data = validate_token(auth.credentials) 
        if data ['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=403, detail='Crendentials no valid')


@app.get('/', tags= ["home"])
def read_root():
    return HTMLResponse('<h1 style="font-family:Arial;color:#229286;text-align:center">Whatsapp Application Contact Data</h1>')

@app.post('/login', tags=['auth'])
def login(user: UserAdmin):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@app.get('/contacts', tags= ['Contacts'], status_code= 200, dependencies= [Depends(JWTBearer())])
def get_contacts():
    if len(data) == 0:
        raise HTTPException(status_code=204, detail="No contacts in your data")
    return data

@app.post('/contacts', tags=['Contacts'], status_code= 201, dependencies= [Depends(JWTBearer())])
def post_contact(contact: Contacts):
    y = str(uuid4())
    contact.id = y
    data.append(contact.dict())
    write_file(data)
    return data

@app.get('/contacts/{id}', tags=['Contacts'], status_code= 200, dependencies= [Depends(JWTBearer())])
def get_movie(id: str):
    contact = list(filter(lambda x: x['id'] == id,data))
    return contact if len(contact) > 0 else JSONResponse(status_code= 404, content= "Contact not found")

@app.delete('/contacts/{id}', tags=['Contacts'], status_code= 200, dependencies= [Depends(JWTBearer())])
def delete_movie(id: str):
    for i in data:
        if i['id']==id:
            data.remove(i)
            write_file(data)
            return data
    raise HTTPException(status_code=404, detail="Contact not found")

@app.put('/contacts/{id}', tags=['Contacts'], status_code= 200, dependencies= [Depends(JWTBearer())])
def update_contact(id: str, contact: Contacts):
    for index, post in enumerate(data):
        if post['id'] == id:
            data[index]['name']= contact.dict()['name']
            data[index]['number']= contact.dict()['number']
            write_file(data)
            return data
    raise HTTPException(status_code=404, detail="Contact not found")
