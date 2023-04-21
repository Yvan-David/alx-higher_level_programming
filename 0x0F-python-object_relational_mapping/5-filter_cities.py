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
    c.execute(""" SELECT cities.name FROM cities
              JOIN states ON state_id = states.id
              AND states.name = '{}'""".format(a[0]))
    print(", ".join(str(i[0]) for i in c.fetchall()))
except IndexError:
    print("sthing is wrong please check your index")
