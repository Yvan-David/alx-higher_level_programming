#!/usr/bin/python3
""" module that lists state name in table states """
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
stat1 = State(name='Louisiana')
stats = session.add(stat1)
session.commit()
