#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa

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
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the State with id = 2
    update_state = session.query(State).filter(State.id == 2).first()

    # Check if the state exists
    if state_to_update:
        # Change the name to 'New Mexico'
        update_state.name = 'New Mexico'
        session.commit()
    else:
        print("State with id = 2 not found.")
