#!/usr/bin/python3
"""Use pure ORM without SQL syntax on cities table"""
from sqlalchemy import Column, ForeignKey, MetaData, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    cities = relationship("City", back_populates="state")


class City(Base):
    """City class:
    inherits from Base"""

    __tablename__ = "cities"

    id = Column(
        Integer, nullable=False, unique=True, autoincrement=True, primary_key=True
    )
    name = Column(String(128), nullable=False)
    states_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")
