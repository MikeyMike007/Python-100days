# Learnings

You can in the HTML code use `{{ wtf.quick_form(form, novalidate=True) }}` to render the whole form you pass into the `render_template` function. Please note that you first need to include following code in the top of the HTML file you are rendering,

```jinja2
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}
```

You also need to import following into python `from flask_bootstrap import Bootstrap`

Its important that you secure your HTTP requests with `CSRF`. See: https://flask-wtf.readthedocs.io/en/1.0.x/csrf/

## Example app with cafe data

./server.py

```python
from os import error
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = StringField("Open time e.g. 8 AM", validators=[DataRequired()])
    close_time = StringField("Close time e.g. 5 PM", validators=[DataRequired()])
    coffe_rating = SelectField(
        "Coffe Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()],
    )

    wifi_rating = SelectField(
        "Wifi Rating",
        choices=["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )

    power_outlet_rating = SelectField(
        "Power Outlet Rating",
        choices=["✘", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("db.csv", "a") as data:
            writer = csv.writer(data)
            writer.writerow(
                [
                    form.cafe.data,
                    form.location.data,
                    form.open_time.data,
                    form.close_time.data,
                    form.coffe_rating.data,
                    form.wifi_rating.data,
                    form.power_outlet_rating.data,
                ]
            )
            return redirect(url_for("cafes"))

    return render_template("add.html", form=form)

@app.route("/cafes")
def cafes():
    with open("db.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)

if __name__ == "__main__":
    app.run(debug=True)
```

./templates/index.html

```jinja2
{% extends 'bootstrap/base.html' %}

{% block title %}Coffee and Wifi{% endblock %}

{% block content %}
  <div class="jumbotron text-center">
      <div class="container">
    <h1 class="display-4">☕️ Coffee & Wifi 💻</h1>
    <p class="lead">Want to work in a cafe but need power and wifi?</p>
    <hr class="my-4">
    <p>You've found the right place! Checkout my collection of cafes with data on power socket availability, wifi speed and coffee quality.</p>
    <a class="btn btn-warning btn-lg" href="{{url_for('cafes')}}" role="button">Show Me!</a>
  </div>
  </div>

{% endblock %}
```

./templates/add.html

```jinja2
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Add A New Cafe{% endblock %}

{% block content %}
<div class="container">
  <div class="row">
    <div class="col-sm-12 col-md-8">

      <h1>Add a new cafe into the database</h1>
      {{ wtf.quick_form(form, novalidate=True) }}

      <p class="space-above"><a href="{{url_for('cafes')}}">See all cafes</a></p>

    </div>
  </div>
</div>
{% endblock %}
```

./templates/cafes.html

```jinja2
{% extends 'bootstrap/base.html' %}

{% block styles %}
{{ super() }}
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Restaurants{% endblock %}

{% block content %}

<div class="container">
  <div class="row">
    <div class="col-sm-12">

      <h1>All Cafes</h1>

      <table class="table">

      {% for row in cafes %}
        <tr>
            {% for item in row %}
              {% if item[0:4] == "http" %}
                <td><a href="{{ item }}">Maps Link</a></td>
              {% else %}
                <td>{{ item }}</td>
              {% endif %}
            {% endfor %}
          </tr>
        {% endfor %}
      </table>
      <p><a href="{{ url_for('home') }}">Return to index page</a></p>
    </div>
  </div>
</div>
{% endblock %}
```

./static/css/styles.css

```css
/* This CSS file will need to be added to the styling of 
your web pages for the styles to be rendered. */

body {
  background-color: #333;
  color: white;
}

a {
  color: #ffc107;
}

.jumbotron {
  display: flex;
  align-items: center;
  margin: 0;
  height: 100vh;
  color: white;
  background-color: #333;
}

.space-above {
  margin-top: 20px;
  padding-top: 20px;
}
```
