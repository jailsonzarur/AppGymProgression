from fastapi import FastAPI
from src.routers import auth
from src.infra.orm.config.database import create_db

app = FastAPI()
create_db()

app.include_router(auth.router)