#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
for listing all states in the database
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
           user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    users = cur.fetchall()

    for user in users:
        print(user)

    cur.close()
    db.close()

