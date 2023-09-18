#!/usr/bin/python3

""" Definition for the class model """

from model_state import Base, Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    __tablename__ = 'cities'
    id = Column(
            Integer(), autoincrement=True, nullable=False,
            primary_key=True, unique=True)
    name = Column(
            String(128), nullable=False)
    state_id = Column(
            Integer(), ForeignKey("states.id"), nullable=False)
