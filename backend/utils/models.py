from sqlalchemy.orm import declarative_base
from sqlalchemy import DECIMAL, TIMESTAMP, Boolean, create_engine, Column, Integer, VARCHAR, Text, ForeignKey
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


class UsersNotify(Base):
    __tablename__ = 'users_notify'

    id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),
                nullable=False, index=True)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    text = Column(Text, nullable=False)
    public_time = Column(TIMESTAMP, nullable=True)
    is_repost = Column(Boolean, nullable=False, default=False)
    repost_text = Column(Text, nullable=True)
    repost_author = Column(VARCHAR(255), nullable=True)
    repost_url = Column(VARCHAR(255), nullable=True)
