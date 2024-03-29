#!/usr/bin/python3

"""
Script that lists all State objects
and corresponding City objects, contained
in the database hbtn_0e_101_usa

args: <mysql username> /
      <mysql password> /
      <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Use a single query to retrieve states and cities with relationship
    data = session.query(State).order_by(State.id).all()

    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
