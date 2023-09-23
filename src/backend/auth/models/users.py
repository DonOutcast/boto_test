from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from database.connection import Base
from auth.models.users_roles import users_roles


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100))
    email = Column(String(50), unique=True)
    person_id = Column(Integer, ForeignKey('person.id'))

    person = relationship('Person', back_populates='users')

    roles = relationship("Role", secondary=users_roles, back_populates="users")
