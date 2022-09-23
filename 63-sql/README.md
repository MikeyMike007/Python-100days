# Learnings

## Flask SQLAlchemy

### Initate a database

```python
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
```

### Define a table in the database

```python
class Book(db.Model):
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(250), unique=True, nullable=False)
author = db.Column(db.String(250), nullable=False)
rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"
```

### Create database and table

This should only be used at the first time when you run your app. Delete / comment afterward.

```python
db.create_all()
```

### Create a new item (book) inside table

```python
book_form = BookForm()
book_form.validate_on_submit()
if book_form.validate_on_submit():
new_book = Book(title=book_form.name.data, author=book_form.author.data, rating=float(book_form.rating.data),
)
db.session.add(new_book)
db.session.commit()
```

### Update a item in table

```python
book_to_update = Book.query.get(book_id)
form = EditBookForm()
if form.validate_on_submit():
book_to_update.rating = float(form.rating.data)
db.session.commit()
```

### Delete an item in table

```python
book_to_delete = Book.query.get(book_id)
form = DeleteBookForm()
if form.validate_on_submit():
db.session.delete(book_to_delete)
db.session.commit()
```

### Retrieve all items in table

```python
all_books = db.session.query(Book).all()
```

## App example with SQLAlchemy and Sqlite

./server.py

```python
from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, Form, SubmitField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import os

class DeleteBookForm(FlaskForm):
    submit = SubmitField(label="Submit")

class BookForm(FlaskForm):
    name = StringField(label="Book name", validators=[DataRequired()])
    author = StringField(label="Book Author", validators=[DataRequired()])
    rating = StringField(label="Rating", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

class EditBookForm(FlaskForm):
    rating = StringField(label="New Rating", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

all_books = []

# Create Database
# ------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# ------------------------

# Create Table
# ------------------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"

db.create_all() # Use only first time you are running app. Then comment out
# ------------------------

@app.route("/edit/<int:book_id>", methods=["POST", "GET"])
def edit(book_id):
    book_to_update = Book.query.get(book_id)
    form = EditBookForm()
    if form.validate_on_submit():
        book_to_update.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, book=book_to_update)

@app.route("/delete/<int:book_id>", methods=["POST", "GET"])
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    form = DeleteBookForm()
    if form.validate_on_submit():
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("delete.html", form=form, book=book_to_delete)

@app.route("/")
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    book_form = BookForm()
    book_form.validate_on_submit()
    if book_form.validate_on_submit():
        new_book = Book(
            title=book_form.name.data,
            author=book_form.author.data,
            rating=float(book_form.rating.data),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=book_form)

if __name__ == "__main__":
    app.run(debug=True)
```

./templates/index.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Library</title>
  </head>
  <body>
    <h1>My Library</h1>
    <ul>
      {% for book in books %}
      <li>
        {{book["title"]}} - {{book["author"]}} - {{book["rating"]}}
        <a href="{{url_for('edit', book_id=book["id"])}}">Edit</a> -
        <a href="{{url_for('delete', book_id=book["id"])}}">Delete</a>
      </li>
      {% endfor %}
    </ul>

    <a href="{{url_for('add_book')}}">Add New Book</a>
  </body>
</html>
```

./templates/add.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Add Book</title>
  </head>
  <body>
    <form method="POST" action="{{url_for('add_book')}}" novalidate>
      {{ form.csrf_token }}
      {{form.name.label}} {{form.name()}}
      {{form.author.label}} {{form.author()}}
      {{form.rating.label}} {{form.rating()}}
      {{form.submit()}}
    </form>
  </body>
</html>


```

./templates/edit.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Library</title>
  </head>
  <body>
    <h1>Edit Rating</h1>

    <h1>Change rating of {{book.title}}. Current rating is {{book.rating}}.</h1>
    <h2>Book id {{book.id}}</h2>

    <form
      method="POST"
      action="{{url_for('edit', book_id = book.id)}}"
      novalidate
    >
      {{ form.csrf_token }}
      {{form.rating.label}} {{form.rating()}}
      {{form.submit()}}
    </form>
    <a href="{{url_for('add_book')}}">Add New Book</a>
  </body>
</html>
```

./templates/delete.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Delete book</title>
  </head>
  <body>
    <h1>Delete book</h1>

    <h1>Are you sure you want to delete {{book.title}}.</h1>
    <h2>Book id {{book.id}}</h2>

    <form
      method="POST"
      action="{{url_for('delete', book_id = book.id)}}"
      novalidate
    >
      {{ form.csrf_token }}
      {{form.submit()}}
    </form>
    <a href="{{url_for('home')}}">Home</a>
  </body>
</html>
```
