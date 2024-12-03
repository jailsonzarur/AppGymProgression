from src.infra.orm.config.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

# Usuário
class User( Base ):
    __tablename__ = "users"

    #USERNAME e EMAIL são únicos por Usuário
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_activate: Mapped[bool] = mapped_column(nullable=False)

    planilhas = relationship("Planilha", back_populates="user")

#Planilha
class Planilha( Base ):
    __tablename__ = "planilhas"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    user = relationship("User", back_populates="planilhas")


