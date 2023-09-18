#!/usr/bin/python3

""" script that prints the first sate object form the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Session = sessionmaker(engine)
    localSession = Session()

    output = localSession.query(State).first()
    if output is None:
        print("Nothing")
    else:
        print(f"{output.id}: {output.name}")
    localSession.close()
