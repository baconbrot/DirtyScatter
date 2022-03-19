from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Session = sessionmaker()
engine = create_engine('sqlite:///db.db',echo=False,future=True)
Session.configure(bind=engine, future=True)
Base = declarative_base()
from dirtyscatter.db.orm import History
from dirtyscatter.db.orm import User
Base.metadata.create_all(engine)