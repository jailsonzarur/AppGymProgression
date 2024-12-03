from src.schemas import schemas
from src.infra.orm.models import models
from uuid import uuid4
from sqlalchemy.orm import Session

class UserRepositorie:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.User):
        user = models.User(id=str(uuid4()), username=user.username, email=user.email, 
                           password=user.password, is_activate=True)
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def get_user_by_id(self, user_id: str):
        user = self.db.query(models.User).filter(models.User.id == user_id).first() 
        return user
    
    def get_user_by_username(self, username: str):
        user = self.db.query(models.User).filter(models.User.username == username).first() 
        return user
    
    def get_user_by_email(self, email: str):
        user = self.db.query(models.User).filter(models.User.email == email).first() 
        return user