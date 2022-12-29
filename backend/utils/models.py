from sqlalchemy.orm import declarative_base
from sqlalchemy import DECIMAL, Boolean, create_engine, Column, Integer, VARCHAR, Text, ForeignKey
from ..common.settings import *

engine = create_engine(POSTGRESQL_SERVER)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column(VARCHAR(255), nullable=True)
    second_name = Column(VARCHAR(255), nullable=True)
    phone = Column(DECIMAL(30), nullable=False)
    username = Column(VARCHAR(255), nullable=True)
    is_author = Column(Boolean, default=False, nullable=False)
