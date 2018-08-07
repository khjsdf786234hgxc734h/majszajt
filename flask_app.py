from flask                      import Flask, redirect, render_template, request, url_for
from password                   import db_host, db_database, db_user, db_password
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, String, Numeric
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.orm             import exc

app = Flask(__name__)

app.config['DEBUG'] = True

engine = create_engine('mysql+mysqldb://' + db_user + ':' + db_password + '@' + db_host + '/' + db_database , echo = True)

Base = declarative_base()

class Movie(Base):
    __tablename__         = 'tb_movie'
    id                    = Column(String, primary_key = True)
    title_primary         = Column(String)
    title_secondary       = Column(String)
    title_primary_ascii   = Column(String)
    title_secondary_ascii = Column(String)
    year                  = Column(Integer)
    genre                 = Column(String)
    rating                = Column(Numeric(3,1))
    vote                  = Column(Integer)
    country               = Column(String)




Session = sessionmaker(bind = engine)

@app.route('/')
def hello_world():
    return 'Hello from majszajt!'

@app.route('/ajemdibi_szorcs', methods = ['GET', 'POST'])
def ajemdibi_szorcs():

    list_movies = []

    if request.method == 'POST':

        movie_title = request.form['movie_title']
        movie_year  = request.form['movie_year']

        try:
            session = Session()
            list_movies = session.query(Movie.title_primary, Movie.year, Movie.genre, Movie.rating, Movie.vote, Movie.country).\
                filter(Movie.title_primary.ilike('%' + movie_title + '%')).\
                filter(Movie.year==movie_year)
        #except exc.NoResultFound, exc.MultipleResultsFound:
        except exc.SQLAlchemyError:
            session.rollback()

        else:
            session.rollback()

        finally:
            session.close()

        engine.dispose()

    return render_template('ajemdibi_szorcs.html', list_movies = list_movies )



