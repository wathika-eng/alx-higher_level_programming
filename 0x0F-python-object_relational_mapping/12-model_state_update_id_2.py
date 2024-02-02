#!/usr/bin/python3
"""Update a state"""
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

    if not state:
        print("Not found")
    else:
        for s in state:
            print(f"{s.id}: {s.name}")
    session.close()
