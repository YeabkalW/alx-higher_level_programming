#!/usr/bin/python3
"""a python script that lists all states from a database"""

import MySQLdb
import sys

if __name__ == "s__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                        database=database, port=3306,
                        passwd=password, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for i in cur:
        print(i)

    cur.close()
    db.close()
