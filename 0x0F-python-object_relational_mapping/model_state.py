#!/usr/bin/python3
""" module that creates table using sqlalchemy  """
import sys
from sqlalchemy import Column, String, INTEGER, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State class that creates a states table """

    __tablename__ = "states"

    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    UniqueConstraint(id)
    name = Column(String(128), nullable=False)
