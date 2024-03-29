#!/usr/bin/python3
"""list all City objects"""

from model_state import Base, State
from model_city import Base, City
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
    for s in session.query(State).order_by(State.id).all():
        for c in session.query(City).order_by(City.id).all():
            if c.state_id == s.id:
                print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
