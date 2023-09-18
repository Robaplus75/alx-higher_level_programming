#!/usr/bin/python3

"""
script that deletes all state objects with a nme containint the letter
'a' from the database
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

    output = localSession.query(State).filter(State.name.like("%a%"))
    
    for out in output:
        localSession.delete(out)
    localSession.commit()
    localSession.close()
