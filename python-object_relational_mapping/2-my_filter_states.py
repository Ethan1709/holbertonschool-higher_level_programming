#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    connection = MySQLdb.connect(user=username, passwd=password,
                                 db=database, host="localhost",
                                 port=3306)

    cursor = connection.cursor()
    request = "SELECT * FROM states WHERE name = '{}'\
        ORDER BY states.id".format(state_name_searched)
    cursor.execute(request)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
