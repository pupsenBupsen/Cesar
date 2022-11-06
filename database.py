from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database.db")

Base = declarative_base()

class Rot(Base):
    __tablename__ = 'rots'
    rot = Column(Integer, primary_key=True)
    count = Column(Integer, primary_key=True)
