#!/usr/bin/python3
"""a python script that lists all states from a database"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username,
                     database=database, port=3306,
                     passwd=password)

cur = db.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cur.execute(query)

for i in cur:
    print(i)

if __name__ == '__main__':
    pass
