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
