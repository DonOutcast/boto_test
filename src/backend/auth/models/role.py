from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from backend.database.connection import Base
from backend.auth.models.users_roles import users_roles


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, unique=True)

    users = relationship("User", secondary=users_roles, back_populates="roles")
