#!/usr/bin/python3
"""
Defines a model for State.
python file that contains the class definition
of a State and an instance Base = declarative_base().

Inherits from SQLAlchemy Base and connects to the Sql table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class for a state in Sql db

    __tablename__ (str): The name of the Sql table that stores States.
    id (sqlalchemy.Integer): ID of the state 
    name (sqlalchemy.String): Name of the state
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
