from src.schemas import schemas
from src.infra.orm.models import models
from uuid import uuid4
from sqlalchemy.orm import Session

class PlanilhaRepositorie:

    def __init__(self, db: Session):
        self.db = db

    def create_planilha(self, planilha: schemas.Planilha):
        planilha = models.Planilha(id=str(uuid4()), name=planilha.name, description=planilha.description, 
                           user_id="f66f9933-a15a-4ec6-9369-03e4327bbd97")
        
        self.db.add(planilha)
        self.db.commit()
        self.db.refresh(planilha)

        return planilha