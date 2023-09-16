#!/usr/bin/python3

"""
for listing all states in the databse
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connectin to the database
    """
    db = MySQLdb.connect(
            host='localhost', user=argv[1], port=3306,
            password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    users = cur.fetchall()
    for user in users:
        print(user)
    cur.close()
    db.close()
