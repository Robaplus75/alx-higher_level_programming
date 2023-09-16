#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in states table where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_conn = MySQLdb.connect(
            host='localhost', port=3306, user=argv[1], password=argv[2],
            db=argv[3])

    cur = db_conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id;".format(
                argv[4]))

    output = cur.fetchall()

    for out in output:
        print(out)
