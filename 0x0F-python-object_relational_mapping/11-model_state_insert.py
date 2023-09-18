#!/usr/bin/python3

"""
write a script that adds the state object Louisina to
the database hbtn_03_6_usa
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

    myobj = State(name="Louisiana")
    localSession.add(myobj)
    localSession.commit()

    output = localSession.query(State).filter(
            State.name == "Louisiana").first()
    print(output.id)
    localSession.close()
