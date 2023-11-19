#!/usr/bin/python3
"""
Class that defines a relationship City model.
Inherits from SQLAlchemy Base and connects to the Sql table.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city in Sql db.

    Attributes:
        id (sqlalchemy.Column): ID of city.
        name (sqlalchemy.Column): Nmae of city.
        state_id (sqlalchemy.Column): City's state ID.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
