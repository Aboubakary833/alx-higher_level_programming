#!/usr/bin/python3

"""lists all states starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    filter_value = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}%'
    ORDER BY states.id""".format(filter_value))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
