#!/usr/bin/python3

import MySQLdb
import sys

'''
for listing all states in the database
'''

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(host='localhost', port=3306,
           user=args[1], password=args[2], db=args[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    users = cur.fetchall()

    for user in users:
        print(user)

    cur.close()
    db.close()
