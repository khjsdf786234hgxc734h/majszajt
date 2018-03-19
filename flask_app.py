from flask                      import Flask, redirect, render_template, request, url_for
from password                   import db_host, db_database, db_user, db_password
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy                 import Column, Integer, String
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.orm             import exc

app = Flask(__name__)

engine = create_engine('mysql+mysqldb://' + db_user + ':' + db_password + '@' + db_host + '/' + db_database , echo = True)

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'tb_movie'
    id = Column(String, primary_key = True)
    title_primary = Column(String)

Session = sessionmaker(bind = engine)

session = Session()

@app.route('/')
def hello_world():
    return 'Hello from majszajt!'

@app.route('/ajemdibi_szorcs', methods = ['GET', 'POST'])
def imdb_search():
    
    list_movies = []
    
    if request.method == 'GET':
        return render_template('movie_search.html', list_movies = list_movies)

    try:
        #session = Session()
        movie_title = request.form['movie_title']
        list_movies = session.query(Movie.title_primary).filter(Movie.title_primary.ilike('%' + movie_title + '%'))
    #except exc.NoResultFound, exc.MultipleResultsFound:
    except exc.SQLAlchemyError:
#        list_movies = []
        pass
    
    else:
        pass
#        list_movies = []

    finally:
#        session.close()
        pass

    return render_template('movie_search.html', list_movies = list_movies ) 


