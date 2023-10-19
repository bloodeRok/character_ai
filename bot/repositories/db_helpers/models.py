from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .connect_to_db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'web_app_user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    surname = Column(String)
    character = Column(String, default='')
    time = Column(DateTime, default=datetime.now)
    Base.metadata.create_all(engine)
