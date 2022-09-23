# Learnings

## CKEditorField and CKEditor

Editor on a HTML page:

Add this to your `FlaskForm`:

```python
body = CKEditorField("Blog Content", validators=[DataRequired()])
```

Add this to HTML:

```jinja2
{{ckeditor.load()}}
{{ckeditor.config(name='body')}}
```

## Render blogpost as text and not as HTML

Use `safe`:

`{{post.body | safe}}`

## Blog API App

```python
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/new", methods=["POST", "GET"])
def new():
    form = CreatePostForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        now = datetime.now()

        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=f"{now.year}-{now.month}-{now.day}",
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, is_edit=0)

@app.route("/")
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("make-post.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/delete/<int:id>")
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body,
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.body = edit_form.body.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=edit_form, is_edit=1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

.template/make-post.html

```jinja2
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block content %}
{% include "header.html" %}
  <!-- Page Header -->
  <header class="masthead" style="background-image: url('{{ url_for('static', filename='img/edit-bg.jpg')}}')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="page-heading">
            {% if is_edit == 1 %}
              <h1>Edit Post</h1>
            {% else %}
              <h1>New Post</h1>
            {% endif%}
            <span class="subheading">You're going to make a great blog post!</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">

          <!-- This is where the form will go -->
          <form action="{{url_for('new')}}" novalidate method="POST">
            {{form.csrf_token}}
            {{wtf.quick_form(form)}}

          {{ckeditor.load()}}
          {{ckeditor.config(name='body')}}
          </form>

      </div>
    </div>
  </div>

{% include "footer.html" %}
{% endblock %}
```

./templates/post.html

```jinja2
{% include "header.html" %}

<!-- Page Header -->
<header class="masthead" style="background-image: url('{{post.img_url}}')">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-heading">
          <h1>{{post.title}}</h1>
          <h2 class="subheading">{{post.subtitle}}</h2>
          <span class="meta"
            >Posted by
            <a href="#">{{post.author}}</a>
            on {{post.date}}</span
          >
        </div>
      </div>
    </div>
  </div>
</header>

<!-- Post Content -->
<article>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <p>{{post.body | safe}}</p>
        <hr />
        <div class="clearfix">
          <a
            class="btn btn-primary float-right"
            href="{{url_for('edit_post', post_id=post.id)}}"
            >Edit Post</a
          >
        </div>
      </div>
    </div>
  </div>
</article>

<hr />
{% include "footer.html" %}
```
