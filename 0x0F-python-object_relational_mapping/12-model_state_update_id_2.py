#!/usr/bin/python3

"""
Script that changes the name of a State
object from the database hbtn_0e_6_usa

args: <mysql username> /
      <mysql password> /
      <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
