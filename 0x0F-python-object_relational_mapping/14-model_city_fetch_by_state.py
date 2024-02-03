#!/usr/bin/python3
"""Fetch data from DB using ORM"""
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

    states = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id
    )

    for state_name, city_id, city_name in states:
        print(f"{state_name}: ({city_id}) {city_name} ")

    session.close()
