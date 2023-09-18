#!/usr/bin/python3

""" script that prints all city objects form the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Session = sessionmaker(engine)
    localSession = Session()

    output = localSession.query(City, State).join(State)

    for out in output:
        print("{}: ({}) {}".format(
            out[1].name, out[0].id, out[0].name))

    localSession.close()
