#!/usr/bin/python3
"""States class"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    result = engine.execute(text("SELECT * FROM states;"))
    row = result.fetchone()
    if row is not None:
        print("{}: {}".format(row[0], row[1]))
    else:
        print("Nothing")