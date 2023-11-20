#!/usr/bin/python3

"""
Script that lists all City objects
from the database hbtn_0e_101_usa

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

    data = session.query(City).join(State).order_by(City.id)

    for city in data:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
