from flask                      import Flask, render_template, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, String, Numeric
from majszajt                   import db_session as session

app = Flask(__name__)

app.config['DEBUG'] = True



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


@app.route('/')
def hello_world():
    return 'Hello from ...'


@app.route('/ajemdibi_szorcs', methods = ['GET', 'POST'])
def ajemdibi_szorcs():

    list_movies = []

    if request.method == 'POST':

        movie_title = request.form['movie_title']
        movie_year  = request.form['movie_year']
        movie_genre = request.form['movie_genre']

        try:
            list_movies = session.query(Movie.id, Movie.title_primary, Movie.year, Movie.genre, Movie.rating, Movie.vote, Movie.country).\
                filter(Movie.title_primary.ilike('%' + movie_title + '%')).\
                filter(Movie.genre.ilike('%' + movie_genre + '%')).\
                filter(Movie.year==movie_year)
            session.rollback()
        except:
            session.rollback()
        finally:
            session.rollback()

    return render_template('ajemdibi_szorcs.html', list_movies = list_movies )



