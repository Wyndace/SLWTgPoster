from sqlalchemy.orm import declarative_base
from sqlalchemy import DECIMAL, Boolean, create_engine, Column, Integer, VARCHAR, Text, ForeignKey
from ..common.settings import *

engine = create_engine(POSTGRESQL_SERVER)
Base = declarative_base()
