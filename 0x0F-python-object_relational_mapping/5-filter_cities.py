#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state"""

import MySQLdb
import sys


def protect(str):
    """Protects database from SQL injection"""
    proof = str.replace(";", "';").replace("\\", "\\\\").replace("'", "''")
    return proof


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
statename = protect(sys.argv[4])

db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, database=database,
                     port=3306)

cur = db.cursor()
query = "SELECT cities.name FROM cities JOIN states\
         ON cities.state_id = states.id WHERE states.name LIKE '%s' ORDER\
         BY cities.id ASC;" % statename
cur.execute(query)

cities = []
for i in cur:
    cities.append(i[0])

print(", ".join(cities))

cur.close()
db.close()

if __name__ == '__main__':
    pass
