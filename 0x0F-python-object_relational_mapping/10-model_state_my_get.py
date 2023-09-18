#!/usr/bin/python3
"""
script that prints th eState object with the name passed as
argument form oth database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Session = sessionmaker(engine)
    localSession = Session()

    output = localSession.query(State).filter(State.name == argv[4]).first()

    if output is None:
        print("Not found")
    else:
        print(output.id)

    localSession.close()
