from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from Forms import RateMovieForm, AddMovieForm
import requests

TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
TMDB_MOVIE_URL = 'https://api.themoviedb.org/3/movie/'
TMDB_IMG_URL = 'https://image.tmdb.org/t/p/original'
TMDB_API = 'TMDB_API'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
Bootstrap(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


def add_to_db(title, year, description, img_url):
    with app.app_context():
        movie = Movie(
            title=title,
            year=year,
            description=description,
            img_url=img_url,
        )
        db.session.add(movie)
        db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(url=TMDB_SEARCH_URL, params={"api_key": TMDB_API, "query": title})
        data = response.json()['results']
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route('/find', methods=['GET', 'POST'])
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        api_call = TMDB_MOVIE_URL + movie_id
        response = requests.get(url=api_call, params={"api_key": TMDB_API, "language": 'en-US'})
        data = response.json()
        title = data["title"]
        img_url = TMDB_IMG_URL + data["poster_path"]
        year = data["release_date"].split('-')[0]
        description = data["overview"]
        with app.app_context():
            movie = Movie(
                title=title,
                year=year,
                description=description,
                img_url=img_url,
            )
            db.session.add(movie)
            db.session.commit()
            return redirect(url_for("rate_movie", id=movie.id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
