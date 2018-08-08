from password import db_host, db_database, db_user, db_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import g


engine = create_engine('mysql+mysqldb://' + db_user + ':' + db_password + '@' + db_host + '/' + db_database , echo = True)

if not g.db_session:
    g.db_session = sessionmaker(bind = engine)





