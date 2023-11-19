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
    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
    for city in state.cities:
        print("    {}: {}".format(city.id, city.name))
