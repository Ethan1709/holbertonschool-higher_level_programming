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
    state_searched = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    r = engine.execute("SELECT states.id FROM states WHERE name = %s", (state_searched,))
    if r.rowcount > 0:
        for row in r:
            print(row[0])
    else:
        print("Not found")
