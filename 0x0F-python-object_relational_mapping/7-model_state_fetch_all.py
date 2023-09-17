#!/usr/bin/python3

"""
script that lists all state object form the databse
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Session = sessionmaker(engine)

    localSession = Session()

    mystates = localSession.query(State).order_by(State.id).all()

    for state in mystates:
        print(f"{state.id}: {state.name}")

    localSession.close()
