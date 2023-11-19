#!/usr/bin/python3

"""
Script that Lists all State
objects from the database hbtn_0e_6_usa.

args: <mysql username> /
      <mysql password> /
      <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
