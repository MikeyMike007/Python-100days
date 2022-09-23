# Learnings

## Sending mail with python library `smtplib`

Note that in order for this to work with gmail, you first need to approve that third party applications can send email through this account in security settings.

```python
import smtplib
import os

# Get enviroment variables
EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls() # Security layer
        connection.login(EMAIL, EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)
```

## Get enviroment variables

You can set enviroment variables with `export SMTP_SERVER="smtp.gmail.com"` in the terminal

```python
# Get enviroment variables
EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
```

## Send and recieve post request in flask

Send the post request through a HTML form. Note that the name for the input fields are `name` and `email`.

```html
<html>
  <head>
    <title>Signup Letter</title>
  </head>
  <body>
    <h1>Please enter details for letter signup</h1>
    <form action="/signup" method="post">
      <label>Name</label>
      <input type="text" placeholder="name" name="name" />

      <label>Email</label>
      <input type="text" placeholder="email" name="email" />
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>
```

Recieve the post request in the flask app:

```python
# Recieve data from form and render new template
@app.route("/signup", methods=["POST"])
def recieve_data():
    # Note that request is part of Flask - not the requests library
    name = request.form["name"]
    email = request.form["email"]
    return render_template("thank-you.html", name=name, email=email)
```

## Example - Email subscription app

./server.py

```python
from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)

# Get enviroment variables
EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")

@app.route("/")
def home():
    return render_template("index.html")

# Recieve data from form and render new template
@app.route("/signup", methods=["POST"])
def recieve_data():
    # Note that request is part of Flask - not the requests library
    name = request.form["name"]
    email = request.form["email"]
    send_email(name, email, "", "")
    return render_template("thank-you.html", name=name, email=email)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)
```

./templates/index.html

```html
<html>
  <head>
    <title>Signup Letter</title>
  </head>
  <body>
    <h1>Please enter details for letter signup</h1>
    <form action="/signup" method="post">
      <label>Name</label>
      <input type="text" placeholder="name" name="name" />

      <label>Email</label>
      <input type="text" placeholder="email" name="email" />
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>
```

./templates/thank-you.html

```html
<html>
  <head>
    <title>Thank you for signign up newsletter</title>
  </head>
  <body>
    <h1>Thanks for signing up - Information succesfully sent</h1>
    <p>You will soon get your first edition to your mail box</p>
    <h1>Name: {{name}}</h1>
    <h1>Username: {{email}}</h1>
  </body>
</html>
```
