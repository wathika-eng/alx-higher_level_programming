#!/usr/bin/python3
"""Fetch the first instance only"""
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

    states = session.query(State).filter(State.name.like("%a%"))

    if not states:
        print("Nothing")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")

    session.close()
