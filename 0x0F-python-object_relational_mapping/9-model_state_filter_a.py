#!/usr/bin/python3
"""Fetch instances with letter a only"""
from engine import MainEngine
from model_state import State, Base


if __name__ == "__main__":

    Base.metadata.create_all(MainEngine.main_engine)

    states = MainEngine.session.query(State).filter(State.name.like("%a%"))

    if not states:
        print("Nothing")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")

    MainEngine.session.close()
