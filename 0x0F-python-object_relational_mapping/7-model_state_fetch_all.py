#!/usr/bin/python3
"""Use pure ORM without SQL syntax"""
from sqlalchemy import Column, MetaData, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}", pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
    Base.metadata.create_all(engine)

    class State(Base):
        """State class:
        inherits from Base"""

        __tablename__ = "states"

        id = Column(
            Integer, nullable=False, unique=True, autoincrement=True, primary_key=True
        )
        name = Column(String(128), nullable=False)

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.commit()
    session.close()
