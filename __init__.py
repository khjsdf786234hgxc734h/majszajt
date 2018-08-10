from password import db_host, db_database, db_user, db_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
#from flask import g


engine = create_engine('mysql+mysqldb://' + db_user + ':' + db_password + '@' + db_host + '/' + db_database , echo = True)

db_session = scoped_session(sessionmaker(bind = engine))

#if not hasattr(g, 'db_session'):
#    session = sessionmaker(bind = engine)
#    g.db_session = session





