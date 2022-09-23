from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Templates need to be inside folder ./templates
    # Images and css files need to be in the ./static folder
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
