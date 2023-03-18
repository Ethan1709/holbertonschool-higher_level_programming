#!/usr/bin/python3
"""States class"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State).filter(State.id == 1).one()
    if q:
        print("{}: {}".format(q.id, q.name))
    else:
        print("Nothing")
    session.close()
