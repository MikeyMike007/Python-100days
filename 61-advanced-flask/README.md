# Learnings

## WTForms

WTForms is a flexible forms validation and rendering library for Python web development. It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N), and more. There are various community libraries that provide closer integration with popular frameworks.

You need both the libraries `flask_wtf` and `wtforms`.

To create a form, you can create, for example, an own class called `LoginForm` that inherits from class `FlaskForm`. In this class, you can now create your form fields. See example below.

```python
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Length(min=6, max=30), Email()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log in")
```

There are many types of fields that you can import and add. See below for a sample of field types,

```python
wtforms.fields.BooleanField
wtforms.fields.DateField
wtforms.fields.DateTimeField
wtforms.fields.DateTimeLocalField
wtforms.fields.DecimalField
wtforms.fields.DecimalRangeField
wtforms.fields.EmailField
wtforms.fields.FileField
wtforms.fields.MultipleFileField
wtforms.fields.FloatField
wtforms.fields.IntegerField
wtforms.fields.IntegerRangeField
wtforms.fields.RadioField
wtforms.fields.SelectField
wtforms.fields.SearchField
wtforms.fields.SelectMultipleField
wtforms.fields.SubmitField
wtforms.fields.StringField
wtforms.fields.TelField
wtforms.fields.TimeField
wtforms.fields.URLField
wtforms.fields.URLField
wtforms.fields.PasswordField
wtforms.fields.TextAreaField
wtforms.fields.FormField
wtforms.fields.FieldList
```

There are many types of validators as well,

```python
wtforms.validators.DataRequired
wtforms.validators.Email
wtforms.validators.InputRequired
wtforms.validators.IPAddress
wtforms.validators.Length
wtforms.validators.MacAddress
wtforms.validators.NumberRange
wtforms.validators.Optional
wtforms.validators.Regexp
wtforms.validators.URL
wtforms.validators.UUID
wtforms.validators.AnyOf
wtforms.validators.NoneOf
```

To get the error messages from the validator into the HTML document, you first need to pass the form instance to the `render_template` function. Then you can get the error messages with some jinja code. In the case below, the variable `form` is the form instance and `email` is a field instance.

```jinja2
{% for err in form.email.errors %}
```

When the user submits the form, you can use the code `if login_form.validate_on_submit():` to see if the validation has succeded.

Also, to display the forms in the html code you will need to add something like this as an example,

````hinja2
{{ form.password.label }}
{{ form.password() }}
{{ form.submit() }}

## Example app

./server.py

```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
import os

class LoginForm(FlaskForm):
    email = StringField(
        label="Email", validators=[DataRequired(), Length(min=6, max=30), Email()]
    )
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_FLASK_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # If validation is OK!
    if login_form.validate_on_submit():
        # Tap into data sent
        print(login_form.email.data)
        print(login_form.password.data)

        if (
            login_form.email.data == "admin@admin.com"
            and login_form.password.data == "123"
        ):
            return render_template("success.html", form=login_form)

        else:
            return render_template("denied.html", form=login_form)

    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)
````

./templates/base.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>{% block title %}{% endblock %}</title>
    <style>
      {% block styling %}
      body{
          background: purple;
      }
      {% endblock %}
    </style>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

./templates/index.html

```jinja2
<!DOCTYPE html>
<html>
  <head>
    <title>Secrets</title>
  </head>
  <body>
    <div class="jumbotron">
      <div class="container">
        <h1>Welcome</h1>
        <p>Are you ready to discover my secret?</p>
        <form action="{{ url_for('login') }}">
          <input type="submit" clas="btn btn-primary btn-lg" value="Login" />
        </form>
      </div>
    </div>
  </body>
</html>
```

./templates/login.html

```jinja2
<!DOCTYPE html>
<html>
  <head>
    <title>Login</title>
  </head>
  <body>
    <div class="container">
      <h1>Login</h1>
      <form method="POST" action="{{ url_for('login') }}" novalidate>
        {{ form.csrf_token }}
        <p>
          {{ form.email.label }}
          <br>
          {{ form.email(size=30) }}
          {% for err in form.email.errors %}
            <span style="color: red">{{err}}</span>
          {% endfor %}
        </p>
        <p>
          {{ form.password.label }}
          <br>
          {{ form.password(size=30) }}
          {% for err in form.password.errors %}
            <span style="color: red">{{err}}</span>
          {% endfor %}
        </p>
        {{form.submit}}
      </form>
    </div>
  </body>
</html>
```

./templates/denied.html

```jinja2
{% extends "base.html" %}
{% block title %}Access Denied{% endblock %}
{% block styling %}
  {{ super() }}
  h1 { color:red; }
{% endblock %}
{% block content %}
  <div class="container">
    <h1>Access Denied</h1>
    <iframe
      src="https://giphy.com/embed/1xeVd1vr43nHO"
      width="480"
      height="271"
      frameborder="0"
      class="giphy-embed"
      allowfullscreen
    ></iframe>
    <p>
      <a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO"
        >via GIPHY</a
      >
    </p>
  </div>
{% endblock %}
```

./templates/success.html

```jinja2
{% extends "base.html" %}
{% block title %}Success{% endblock %}
{% block content %}
  <div class="container">
    <h1>Top Secret</h1>
    <iframe
      src="https://giphy.com/embed/Ju7l5y9osyymQ"
      width="480"
      height="360"
      frameborder="0"
      class="giphy-embed"
      allowfullscreen
    ></iframe>
    <p>
      <a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a>
    </p>
  </div>
{% endblock %}
```
