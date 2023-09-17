#!/usr/bin/python3

"""
module for class definition
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """Represents the state class"""
    __tablename__ = "states"
    id = Column(Integer(), nullable=False,
            primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
