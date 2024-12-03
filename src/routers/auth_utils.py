from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.infra.providers import token_provider
from src.infra.orm.repositories.user import UserRepositorie
from src.infra.orm.config.database import get_db
from sqlalchemy.orm import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_logged_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    
    try:
        username = token_provider.verify_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido.')
    
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido.')
    
    usuario = UserRepositorie(db).get_user_by_username(username)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    
    return usuario