#!/usr/bin/python3
"""Write a script that lists all City objects from the database hbtn_0e_101_usa"""
from sqlalchemy import create_engine
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City

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

    states = session.query(State).order_by(State.id).all()
    if not states:
        print("nothing found")
    else:
        for state in states:
            for city in state.cities:
                print(f"{city.id}: {city.name} -> {state.name}")

    session.close()
