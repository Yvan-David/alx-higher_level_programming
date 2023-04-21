#!/usr/bin/python3
""" module that lists state name in table states """
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    a = sys.argv[4].split(' ')
    if len(a) != 1:
        raise IndexError
except IndexError:
    print("check your index positions please")


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
stats = session.query(State).filter(State.name == a[0])
count = 0
for stat in stats:
    count = 1
    print(f'{stat.id}')
if count == 0:
    print("Not found")
