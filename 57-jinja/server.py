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
