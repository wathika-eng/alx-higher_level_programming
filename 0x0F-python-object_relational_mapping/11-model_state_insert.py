#!/usr/bin/python3
"""Search the DB"""
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    states = session.query(State).order_by(State.id)

    if not states:
        print("Not found")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")

    session.close()
