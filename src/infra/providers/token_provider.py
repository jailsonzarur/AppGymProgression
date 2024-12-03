from datetime import datetime, timedelta
from jose import jwt
import os

SECRET_KEY = "55dec6cce44eeec107c40c554196cc48"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 300

def create_acess_token(data: dict):
    data = data.copy()
    expiration =  datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)
    
    data.update({"exp": expiration})
    
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    
    return token_jwt

def verify_acess_token(token: str):
    package = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
    return package.get("sub")

