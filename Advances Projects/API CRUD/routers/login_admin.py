from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.schema import UserAdmin
from utils.JWT_manager import create_token

admin_router = APIRouter()

@admin_router.post('/login', tags=['auth'], response_model= UserAdmin)
def login_admin(user: UserAdmin):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content= token)
    