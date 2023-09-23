from datetime import datetime
from enum import Enum as EnumType

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Enum, DateTime

from database.connection import Base


class Sex(EnumType):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    birth = Column(Date)
    sex = Column(Enum(Sex))
    profile = Column(String)
    phone_number = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    users = relationship('Users', back_populates='person')
