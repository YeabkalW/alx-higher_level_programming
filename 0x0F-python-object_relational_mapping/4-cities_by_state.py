#!/usr/bin/python3
"""a script that lists all cities from database"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, database=database,
                     port=3306)

cur = db.cursor()
query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states\
         ON cities.state_id = states.id ORDER BY cities.id ASC;"
cur.execute(query)

for i in cur:
    print(i)

cur.close()
db.close()

if __name__ == "__main__":
    pass
