#!/usr/bin/python3
""" module that lists state name in table states """
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stats = session.query(State).filter(State.name.like('%a%'))
    for stat in stats:
        session.delete(stat)
    session.commit()
except IndexError:
    print('index_error')
