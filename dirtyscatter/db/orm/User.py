from sqlalchemy import Column, String, Integer, select, update

from dirtyscatter.db import Base, Session


class User(Base):
    __tablename__ = 'user'

    name = Column(String(25), primary_key=True)
    rank = Column(Integer)
    scatter = Column(Integer)


def get_all():
    with Session() as session:
        stmt = select(User)
        return session.execute(stmt).all()


def update_user(user, insert=False):
    with Session() as session:
        if not session.get(User, user.name):
            session.add(user)
        else:
            stmt = update(User).where(User.name == user.name).values(rank=user.rank, scatter=user.scatter)
            session.execute(stmt)
        session.commit()


def update_all(users, insert=False):
    for user in users:
        update_user(user, insert=insert)


def get_user_by_name(name):
    with Session() as session:
        return session.get(User, name)


def get_top(number):
    with Session() as session:
        stmt = select(User).order_by(User.rank).limit(number)
        return session.execute(stmt).scalars().all()
