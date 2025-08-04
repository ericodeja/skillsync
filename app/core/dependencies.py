from fastapi.security import OAuth2PasswordBearer
from app.core.role_scopes import all_scopes

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    scopes=all_scopes
)
