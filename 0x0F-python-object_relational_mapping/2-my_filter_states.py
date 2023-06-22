#!/usr/bin/python3
"""srript that takes in an argument and displays all values in the table
where name matches the argument"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
statename = sys.argv[4]

db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, database=database,
                     port=3306)

cur = db.cursor()
query = "SELECT id, name FROM states WHERE name LIKE '%s' ORDER BY id ASC"\
         %statename
cur.execute(query)

for i in cur:
    print(i)

cur.close()
db.close()

if __name__ == "__main__":
    pass
