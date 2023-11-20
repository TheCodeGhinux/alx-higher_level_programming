#!/usr/bin/python3

"""
Script that prints all City objects
from the database hbtn_0e_14_usa

args: <mysql username> /
      <mysql password> /
      <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    """
    Check for correct arguments
    args: Username, password, database, state_name
    """
    username, password, database = sys.argv[1:4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State) \
                  .filter(City.state_id == State.id) \
                  .order_by(City.id)
    for city, state in data:
          print("{}: ({}) {}".format(state.name, city.id, city.name))
