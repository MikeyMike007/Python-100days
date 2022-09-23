# Learnings

## Movie app

./server.py

```python
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
```

./templates/add.html

```jinja2
{% extends 'bootstrap/base.html' %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Add Movie{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">Add a Movie</h1>

    <form action="{{url_for('add')}}" method="POST" novalidate>
    {{ form.csrf_token }}
    {{form.title.label}}
    {{form.title()}}
    {{form.submit()}}

    </form>
</div>
{% endblock %}
```

./templates/edit.html

```jinja2
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Edit Movies{% endblock %}

{% block content %}
<div class="content">
  <h1 class="heading">Movie Title</h1>
    <p class="description">Edit Movie Rating</p>
    <form action="{{url_for('update', id=movie.id)}}" method="POST" novalidate>
    {{ form.csrf_token }}
    {{form.rating.label}}
    {{form.rating()}}
    {{form.review.label}}
    {{form.review()}}
    {{form.submit()}}
    </form>
  </div>
{% endblock %}
```

./templates/index.html

```jinja2
{% extends 'bootstrap/base.html' %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}My Top 10 Movies{% endblock %}

{% block content %}
<div class="container">
  <h1 class="heading">My Top 10 Movies</h1>
  <p class="description">These are my all time favourite movies.</p>

  {% for movie in movies %}
  <div class="card" >
    <div class="front" style="background-image: url('{{movie.img_url}}');">
      <p class="large">{{movie.id}}</p>
    </div>
    <div class="back">
      <div>
        <div class="title">{{movie.title}} <span class="release_date">({{movie.year}})</span></div>
        <div class="rating">
          <label>{{movie.rating}}</label>
          <i class="fas fa-star star"></i>
        </div>
        <p class="review">"{{movie.review}}"</p>
        <p class="overview">
        {{movie.description}}
        </p>

        <a href="{{url_for('update', id=movie.id)}}" class="button">Update</a>
        <a href="{{url_for('delete', id=movie.id)}}" class="button delete-button">Delete</a>

      </div>
    </div>
  </div>
  {% endfor %}
</div>
<div class="container text-center add">
  <a href="{{url_for('add')}}" class="button">Add Movie</a>
</div>
{% endblock %}
```

./templates/select.html

```jinja2
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Select Movie{% endblock %}

{% block content %}
<div class="container">
    <h1 class="heading">Select Movie</h1>
    {% for movie in movies %}
  <p>
  <a href="{{url_for('find', id=movie.id)}}"> {{movie.title}} - {{movie.release_date}}</a>
  </p>

    {% endfor %}

</div>
{% endblock %}


```
