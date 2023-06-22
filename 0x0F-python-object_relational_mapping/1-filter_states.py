#!/usr/bin/python3
"""script that lists all states with a name starting with N from database"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, database=database,
                     port=3306)

cur = db.cursor()
query = ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
cur.execute(query)

for i in cur:
    print(i)

cur.close()
db.close()

if __name__ == "__main__":
    pass
