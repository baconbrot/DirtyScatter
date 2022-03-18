from sqlalchemy import Column, String, Integer

from db import Base, Session


class History(Base):
    __tablename__ = 'user_history'

    name = Column(String(25), primary_key=True)
    timestamp = Column(Integer, primary_key=True)
    scatter = Column(Integer)


def insert_history(history):
    with Session() as session:
        session.add(history)
        session.commit()


def insert_histories(histories):
    with Session() as session:
        session.add_all(histories)
        session.commit()
