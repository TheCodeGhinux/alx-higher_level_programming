#!/usr/bin/python3

"""
Script that deletes all State objects with
a name containing the letter a
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

    """Filter and delete the states directly in the query"""
    delete_state = session.query(State).filter(State.name.like("%a%"))
    for state in delete_state:
        session.delete(state)

    session.commit()
    session.close()
