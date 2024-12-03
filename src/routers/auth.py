from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas import schemas
from src.infra.orm.config.database import get_db
from sqlalchemy.orm import Session
from src.infra.orm.repositories.user import UserRepositorie
from src.infra.providers import hash_provider, token_provider

router = APIRouter(prefix = "/auth", tags = ["Users"])

@router.post("/signup", status_code = status.HTTP_201_CREATED)
def sign_up(user: schemas.User, db: Session = Depends(get_db)):

    verify_user = UserRepositorie(db).get_user_by_username(user.username)

    if verify_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="Usuário já existente")
    
    verify_user = UserRepositorie(db).get_user_by_email(user.email)

    if verify_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="Usuário já existente")
    
    user.password = hash_provider.generate_hash(user.password)

    created_user = UserRepositorie(db).create_user(user)

    return created_user

@router.post("/login", status_code = status.HTTP_200_OK)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    username = user.username
    password = user.password

    user = UserRepositorie(db).get_user_by_username(username)

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuário não existe ou a senha é inválida.")

    valid_password = hash_provider.verify_hash(password, user.password)

    if not valid_password:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuário não existe ou a senha é inválida.")
    
    TOKEN = token_provider.create_acess_token({"sub": username})

    return {"Token": TOKEN}


