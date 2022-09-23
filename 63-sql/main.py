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
