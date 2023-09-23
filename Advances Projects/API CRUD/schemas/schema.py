from typing import Optional
from pydantic import BaseModel, Field


class Users(BaseModel):
    id: Optional[str] = None
    name : str = Field(min_length=4, max_length = 20)
    email : str = Field(min_length=4, max_length = 20)
    password : str = Field(min_length=1, max_length = 100)

    
    model_config ={
        "json_schema_extra": {
            "examples": [
                {
                    "name": "My name",
                    "email": "My email",
                    "password": "My password",
                }
            ]
        }}
    
class UserAdmin(BaseModel):
    email: str
    password: str