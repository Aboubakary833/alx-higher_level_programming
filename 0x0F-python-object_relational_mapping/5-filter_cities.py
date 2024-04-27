#!/usr/bin/python3

"""filter cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON states.id=cities.state_id WHERE
    states.name=%s""", (name, ))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
