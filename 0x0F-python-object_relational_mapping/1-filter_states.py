#!/usr/bin/python3
"""
module for lsitign all states with a name starting
with N form the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(
            host='localhost', port=3306, user=argv[1],
            password=argv[2], db=argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    output = cur.fetchall()

    for out in output:
        print(out)
    cur.close()
    db_conn.close()
