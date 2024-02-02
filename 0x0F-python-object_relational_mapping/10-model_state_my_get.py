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
    search_query = sys.argv[4]

    engine = create_engine(
        f"mysql://{user}:{password}@localhost:3306/{db}", pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    states = (
        session.query(State)
        .filter(
            State.name.like(
                f"%{search_query}%",
            )
        )
        .first()
    )

    if not states:
        print("Not found")
    else:
        print(f"{states.id}")

    session.close()
