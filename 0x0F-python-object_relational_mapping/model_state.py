#!/usr/bin/python3
"""Use pure ORM without SQL syntax"""
from sqlalchemy import Column, MetaData, String, Integer
from sqlalchemy.ext.declarative import declarative_base


# user = sys.argv[1]
# password = sys.argv[2]
# db = sys.argv[3]
# engine = create_engine(
#     f"mysql+mysqldb://{user}{password}@localhost:3306/{db}", pool_pre_ping=True
# )
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State class:
    inherits from Base"""

    __tablename__ = "states"

    id = Column(
        Integer, nullable=False, unique=True, autoincrement=True, primary_key=True
    )
    name = Column(String(128), nullable=False)
