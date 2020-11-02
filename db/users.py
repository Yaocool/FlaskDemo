from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

from settings import SQLALCHEMY_DATABASES

engine = create_engine(SQLALCHEMY_DATABASES['default']['uri'])
Base = declarative_base()


class Users(Base):
    __tablename__ = 'db_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), nullable=False)
    pwd = Column(String(64), nullable=False)
