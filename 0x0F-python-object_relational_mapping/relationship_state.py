#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and
connects to the Sql table for states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a state in db.

    Attributes:
        __tablename__ (str): Name of the table to store States.
        id (sqlalchemy.Integer): Id of state.
        name (sqlalchemy.String): Name of state.
        cities (sqlalchemy.orm.relationship): State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
