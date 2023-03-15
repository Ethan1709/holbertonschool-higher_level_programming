#!/usr/bin/python3
"""States class"""

from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """States class"""
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)