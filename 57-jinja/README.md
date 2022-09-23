# Learnings

Introduction of new flask function `url_for(function_name_api, arg1, arg2, arg3)` where the `args` are arguments to the `function_name_api` function. Works both in python code as well as in Jinja templates (as links).

You could use it as with `redirect(url_for(home))` for example if you want to be redirected to run the function `home`.

## Jinja templates

Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

### Example of Jinja templates

./server.py

```python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    # Now you can catch the passed year variable by typing {{year}} in index.html
    # You can pass as many variables as you want
    return render_template("index.html", year=current_year, next_year=current_year+1)
```

.templates/index.html

```html
<html>
  <head>
    <title>Simple Jinja example</title>
  </head>
  <body>
    <p>Current year: {{year}}</p>
    <p>Next year: {{next}}</p>
  </body>
</html>
```

### Jinja for loops

```jinja2
<ul>
  {% for item in seq %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

### Jinja if statements

```jinja2
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}
```

### Jinja template inheritance

The most powerful part of Jinja is template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

#### Base template

This template, which we’ll call `base.html`, defines a simple HTML skeleton document that you might use for a simple two-column page. It’s the job of “child” templates to fill the empty blocks with content:

./templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
  </head>
  <body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
      {% block footer %} &copy; Copyright 2008 by
      <a href="http://domain.invalid/">you</a>. {% endblock %}
    </div>
  </body>
</html>
```

In this example, the `{% block %}` tags define four blocks that child templates can fill in. All the block tag does is tell the template engine that a child template may override those placeholders in the template.

Block tags can be inside other blocks such as if, but they will always be executed regardless of if the if block is actually rendered.

#### Child template

A child template might look like this:

./templates/child.html

```jinja2
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}
```

The `{% extends %}` tag is the key here. It tells the template engine that this template “extends” another template. When the template system evaluates this template, it first locates the parent. The extends tag should be the first tag in the template. Everything before it is printed out normally and may cause confusion.

## requests module

Requests is an elegant and simple HTTP library for Python, built for human beings.

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data.

### Examples

Response object called `response`. We can get all the information we need from this object.

```python
response = requests.get('https://api.github.com/events')
```

Requests’ simple API means that all forms of HTTP request are as obvious. For example, this is how you make an HTTP POST request.

```python
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
```

You often want to send some sort of data in the URL’s query string. If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. `httpbin.org/get?key=val`. Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument. As an example, if you wanted to pass `key1=value1` and `key2=value2` to `httpbin.org/get`, you would use the following code

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=payload)
print(response.url) # https://httpbin.org/get?key2=value2&key1=value1
```

There’s also a builtin JSON decoder, in case you’re dealing with JSON data:

```python
import requests
r = requests.get('https://api.github.com/events')
r.json()
# [{'repository': {'open_issues': 0, 'url': 'https://github.com/...
```

If you’d like to add HTTP headers to a request, simply pass in a dict to the headers parameter.

```python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

For example, we didn’t specify our user-agent in the previous example:

## Flask example app to ilustrate Jinja templates

./server.py

```python
from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(0, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    # Api endspoints
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url=url).json()
    return render_template("blog.html", posts=all_posts)

@app.route("/guess/<name>")
def guess(name):
    # Api endspoints
    url_age = f"https://api.agify.io?name={name}"
    url_gender = f"https://api.genderize.io?name={name}"

    # Api responses in JSON format
    response_age = requests.get(url=url_age).json()
    response_gender = requests.get(url=url_gender).json()

    # Retrieve estimated gender and age from API
    age_send = response_age["age"]
    gender_send = response_gender["gender"]

    # Data cleaning
    name = name[0].upper() + name[1:]
    gender_send = gender_send[0].upper() + gender_send[1:]

    return render_template(
        "api_response.html", name=name, age=age_send, gender=gender_send
    )

if __name__ == "__main__":
    app.run(debug=True)
```

./templates/index.html

```jinja2
<html>
  <head>
    <title>Hello, World!</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <h2>{{5*6}}</h2>
    <h2>Random number: {{num}}</h2>
    <!-- See method url_for(function_name) to get to blog on the flask server -->
    <a href="{{url_for('get_blog', num=3)}}">Go to blog</a>
  </body>
  <footer>
    <p>Current year: {{year}}</p>
  </footer>
</html>
```

.templates/blog.html

```jinja2
<html>
  <head>
    <title>Test</title>
  </head>
  <body>
    {% for blog_post in posts: %}
      {% if blog_post["id"] == 2 %}
        <h1>{{blog_post["title"]}}</h1>
        <h2>{{blog_post["subtitle"]}}</h2>
        <p>{{blog_post["body"]}}</p>
      {% endif %}
    {% endfor %}
  </body>
</html>
```

.templates/api_response.html

```jinja2
<html>
  <head>
    <title>Test</title>
  </head>
  <body>
    <p><h1>App</h1></p>
    <p>
    <h1>Name: {{name}}</h1>
    <h1>Age: {{age}}</h1>
    <h1>Gender: {{gender}}</h1>

    </p>
  </body>
</html>
```

## Flask app example - Capstone

./server.py

```python
from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog = []
url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(url=url).json()

for post in all_posts:
    blog.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

@app.route("/")
def home():
    return render_template("index.html", posts=blog)

@app.route("/blog/<int:num>")
def get_blog(num):
    post_to_send: Post
    for post in blog:
        if post.id == num:
            post_to_send = post
    return render_template("post.html", post=post_to_send)

if __name__ == "__main__":
    app.run(debug=True)
```

./post.py

```python
class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
```

./templates/index.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="../static/css/styles.css" />
  </head>
  <body>
    <div class="wrapper">
      <div class="top">
        <div class="title"><h1>My Blog</h1></div>
      </div>
      {% for post in posts %}
      <div class="content">
        <div class="card">
          <h2>{{post.title}}</h2>
          <p class="text">{{post.subtitle}}</p>
          <a href="{{url_for('get_blog', num=post.id)}}">Read</a>
        </div>
      </div>
      {% endfor %}
    </div>
  </body>
  <footer>
    <p>Made with ♥️ in London.</p>
  </footer>
</html>


```

./templates/post.html

```jinja2
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Raleway"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="../static/css/styles.css" />
  </head>
  <body>
    <div class="wrapper">
      <div class="top">
        <div class="title"><h1>My Blog</h1></div>
      </div>
      <div class="content">
        <div class="card">
          <h2>{{post.title}}</h2>
          <p>{{post.body}}</p>
        </div>
      </div>
    </div>
  </body>
  <footer>
    <p>Made with ♥️ in London.</p>
  </footer>
</html>


```

./static/css/styles.css

```css
body {
  background: #efeff3;
  margin: 0;
  font-family: "Raleway", sans-serif;
  -webkit-font-smoothing: antialiased;
  color: #212121;
}
.wrapper {
  position: relative;
  clear: both;
  margin: 0 auto 75px auto;
  width: 100%;
  overflow: hidden;
}
.top {
  background: #4e89ae;
  height: 180px;
  border-top: 20px solid #43658b;
}

.top .title {
  width: 700px;
  margin: 38px auto 0 auto;
}

.title h1 {
  font-size: 24px;
  color: #fff;
  font-weight: 500;
}

.content {
  margin: -80px auto 100px;
  padding-bottom: 20px;
}

.card {
  position: relative;
  background: #fff;
  padding: 50px;
  width: 600px;
  margin: 20px auto 0 auto;
  box-shadow: 0 2px 4px rgba(100, 100, 100, 0.1);
}

.card h2 {
  font-size: 21px;
  font-weight: 500;
}

.card h2 a {
  color: #cc0000;
  text-decoration: none;
}

.card .text {
  color: #212121;
  margin-top: 20px;
  font-size: 15px;
  line-height: 22px;
}

footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #43658b;
  color: white;
  text-align: center;
}
```
