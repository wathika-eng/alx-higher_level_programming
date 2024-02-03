#!/usr/bin/python3
"""
Write a script that deletes all State objects with 
a name containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql://{user}:{password}@localhost:3306/{db}", pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
