from fastapi import FastAPI, Depends
from src.schemas import schemas
from src.infra.orm.repositories.user import UserRepositorie
from src.infra.orm.repositories.planilha import PlanilhaRepositorie
from src.infra.orm.config.database import get_db, create_db
from sqlalchemy.orm import Session


app = FastAPI()

@app.post('/user')
def create_user_route(user: schemas.User, db: Session = Depends(get_db)):
    user = UserRepositorie(db).create_user(user)
    return user

@app.post('/planilha')
def create_planilha_route(planilha: schemas.Planilha, db: Session = Depends(get_db)):
    planilha = PlanilhaRepositorie(db).create_planilha(planilha)
    return planilha