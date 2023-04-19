#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa

"""
import MySQLdb
import sys
try:
    a = sys.argv[4].split(' ')
    if len(a) != 1:
        raise IndexError
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    c = db.cursor()
    c.execute(""" SELECT id, name FROM states WHERE BINARY name LIKE '{}'
              ORDER BY id """.format((a[0])))
    for i in c.fetchall():
        print(i)
except IndexError:
    print("unidentified arguments given")
