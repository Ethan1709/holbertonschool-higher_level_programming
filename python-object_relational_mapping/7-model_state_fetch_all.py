#!/usr/bin/python3
"""States class"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    result = engine.execute(text("SELECT * FROM states;"))
    for row in result.fetchall():
        print("{}: {}".format(row[0], row[1]))