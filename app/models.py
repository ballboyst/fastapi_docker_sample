from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean


Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    email = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    done = Column(Boolean)
    deadline = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
