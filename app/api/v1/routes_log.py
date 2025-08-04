from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.auth import authenticate_user
from app.crud.token import create_access_token, create_refresh_token
from app.schemas.token import Token
from app.core.role_scopes import role_scope_map


router = APIRouter()


@router.post('/login', response_model=Token)
def login_route(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    user = authenticate_user(email, password)

    scopes = role_scope_map[user.role]
    access_token = create_access_token(user, scopes)
    refresh_token = create_refresh_token(user)

    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}
