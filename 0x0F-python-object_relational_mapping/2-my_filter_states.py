#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa

"""
import MySQLdb
import sys
try:
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    c = db.cursor()
    c.execute(""" SELECT id, name FROM states WHERE BINARY name LIKE '{}' ORDER BY id """.format((sys.argv[4])))
    for i in c.fetchall():
        print(i)
except IndexError:
    print("no arguments given")
