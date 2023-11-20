#!/usr/bin/python3
"""
Class definition of a City.
A Python file containing the class definition
of a City and an instance `Base = declarative_base()`.

Inherits from SQLAlchemy `Base` and connects to the SQL table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()

class City(Base):
    """
    Class representing a City in the SQL database.

    Attributes:
    - __tablename__ (str): The name of the SQL table that stores cities.
    - id (sqlalchemy.Integer): ID of the city.
    - name (sqlalchemy.String): Name of the city.
    - state_id (sqlalchemy.String): ID of the City's state.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
