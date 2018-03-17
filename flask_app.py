from flask                      import Flask
from password                   import db_host, db_database, db_user, db_password
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy                 import Column, Integer, String
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.orm             import exc
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from majszajt!'

@app.route('/ajemdibi_szorcs')
def imdb_search():
    engine = create_engine('mysql+mysqldb://' + db_user + ':' + db_password + '@' + db_host + '/' + db_database , echo = True)
    Base = declarative_base()
    class Movie(Base):
        __tablename__ = 'tb_movie'

        id = Column(String, primary_key = True)
        title_primary = Column(String)

    Session = sessionmaker(bind = engine)
    session = Session()
    
    try:
        idd = session.query(Movie.title_primary).filter(Movie.title_primary.ilike('%XXXiger%')).first()
    #except exc.NoResultFound, exc.MultipleResultsFound:
    except exc.SQLAlchemyError:
        idd = 'ERROR :-)'
    else:
        idd = 'Error 2'

    session.close()

    return idd





