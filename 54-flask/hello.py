from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"


@app.route("/bye-bye")
def good_bye():
    return "<h1>Goodbye!</h1>"


if __name__ == "__main__":
    print(time.__name__)  # time - Name of module
    print(__name__)  # __main__ - prints main in case this file is run

    app.run()
