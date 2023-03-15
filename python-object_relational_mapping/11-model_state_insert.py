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

    query = "SELECT * FROM State ALTER TABLE State ADD Louisania"
    r = engine.execute(query)

    for row in r.fetchall():
        print(f"{row[0]: {row[1]}}")
