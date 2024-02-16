#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name".format(args[0]))
    exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT cities.name FROM cities WHERE state_id =\
            (SELECT id FROM states WHERE name LIKE BINARY %s)\
             ORDER BY cities.id;", (state_name, ))
    rows = cur.fetchall()
    k = 1
    for row in rows:
        print(row[0], end='')
        if k < num_rows:
            print(end=', ')
        k += 1
    print()
    cur.close()
    db.close()
