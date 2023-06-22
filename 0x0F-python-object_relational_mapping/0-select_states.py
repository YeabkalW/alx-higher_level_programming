#!/usr/bin/python3
"""a python script that lists all states from a database"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQL.connect(host='localhost', user=username,
                   database=database, port=3306,
                   passwd=password)

cur = db.cursor()
sorted_table = cur.excute("SELECT * FROM states ORDERED BY id ASC")

for i in sorted_table:
    print(i)
    
if __name__ == '__main__':
