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
    args: Username, password, database
    """
    # Extracting MySQL credentials from command line arguments
    username, password, database = sys.argv[1:4]

    # Creating the SQLAlchemy engine with pool_pre_ping
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Binding the engine to the Base class to create tables
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying City and State objects, filtering by state_id, and ordering by City id
    data = session.query(City, State) \
                  .filter(City.state_id == State.id) \
                  .order_by(City.id)

    # Printing the results
    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
