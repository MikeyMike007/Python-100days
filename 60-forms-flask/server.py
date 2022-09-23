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
    # send_email(name, email, "", "")
    return render_template("thank-you.html", name=name, email=email)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
