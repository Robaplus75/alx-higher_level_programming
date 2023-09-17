#!/usr/bin/python3
"""
script that takes int hte name of a state as an argument
and lsits all cities of that state
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    count = 0
    db_conn = MySQLdb.connect(
            host="localhost", charset="utf8", user=argv[1],
            password=argv[2], db=argv[3], port=3306)
    cur = db_conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    output = cur.fetchall()

    for out in output:
        if out[2] == argv[4]:
            if count > 0:
                print(", ", end="")
            print(out[1], end="")
            count = count + 1
    print()
    cur.close()
    db_conn.close()
