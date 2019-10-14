from flask                      import Flask, render_template, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, String, Numeric
from sqlalchemy                 import or_, and_
from majszajt                   import db_session as session
from config                     import ip_allowed

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
    #return str(request.remote_addr) -- did not work
    #return request.environ['REMOTE_ADDR'] -- did not work
    return 'Your IP: ' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

@app.route('/bukmark', methods = ['GET', 'POST'])
def bukmark():
    ip_current = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if ip_current not in ip_allowed:
        return 'Your IP: ' + ip_current

    if request.method == 'POST':
        ip_current = ip_current # to be continued from here

    return render_template('bukmark.html')


@app.route('/ajemdibi_szorcs', methods = ['GET', 'POST'])
def ajemdibi_szorcs():

    list_movies = []

    if request.method == 'POST':

        movie_title = request.form['movie_title']
        movie_title = movie_title.strip()
        movie_year  = request.form['movie_year']
        movie_genre = request.form['movie_genre']

        try:
            list_movies = session.query(Movie.id, Movie.title_primary, Movie.year, Movie.genre, Movie.rating, Movie.vote, Movie.country).\
                filter(or_(Movie.title_primary_ascii.ilike('%' + movie_title + '%'),  Movie.title_secondary_ascii.ilike('%' + movie_title + '%') )).\
                filter(or_(Movie.genre.ilike('%' + movie_genre + '%'), 'Any' == movie_genre )).\
                filter(or_(Movie.year == movie_year, 'Any' == movie_year )).\
                filter(and_(Movie.country.notilike('%bangladesh%'), Movie.country.notilike('%india%'))).\
                filter(and_(Movie.country.notilike('%pakistan%'), Movie.country.notilike('%myanmar%'))).\
                filter(and_(Movie.country.notilike('%indonesia%'), Movie.country.notilike('%philippines%'))).\
                order_by(Movie.rating.desc(), Movie.title_primary.asc())
            session.rollback()
        except:
            session.rollback()
        finally:
            session.rollback()

    return render_template('ajemdibi_szorcs.html', list_movies = list_movies )



