#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
db = MySQLdb.connect (user = f"{sys.argv[1]}", database = f"{sys.argv[2]}")
c = db.cursor()
c.execute (""" SELECT id, name FROM states """)
for i in c.fetchall():
    print(i)
