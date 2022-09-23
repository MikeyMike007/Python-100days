from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, URL
import requests
from flask_sqlalchemy import SQLAlchemy
import os


API_KEY = os.environ.get("MOVIEDB_API_KEY")
MOVIE_API_URL = "https://api.themoviedb.org/3/search/movie/"
SPECIFIC_MOVIE_ENDPOINT = "https://api.themoviedb.org/3/movie/"
IMAGE_ENDPOINT = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])


class AddForm(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)


db.create_all()

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html", movies=movies)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    movie = Movie.query.get(id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/select/<title>", methods=["GET", "POST"])
def select(title):
    params = {"api_key": API_KEY, "query": title}
    response = requests.get(url=MOVIE_API_URL, params=params).json()["results"]
    return render_template("select.html", movies=response)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data.split(" ")
        title = "+".join(title)
        print("I am here")
        return redirect(url_for("select", title=title))
    return render_template("add.html", form=form)


@app.route("/find/<int:id>")
def find(id):
    url = f"{SPECIFIC_MOVIE_ENDPOINT}{id}"
    params = {"api_key": API_KEY}
    response = requests.get(url=url, params=params).json()
    movie = Movie(
        title=response["original_title"],
        year=response["release_date"],
        description=response["overview"],
        rating=float(response["vote_average"]),
        ranking=0,
        review="",
        img_url=f"{IMAGE_ENDPOINT}{response['poster_path']}",
    )

    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
