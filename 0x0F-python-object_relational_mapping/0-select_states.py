#!/usr/bin/python3
"""a python script that lists all states from a database"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=username,
                        database=database, port=3306,
                        passwd=password)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for i in rows:
        print(i)

cur.close()
db.close()
