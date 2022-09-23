from flask import Flask

app = Flask(__name__)


# Get arguments
@app.route("/username/<name>")
def greet(name):
    return (
        f'<h1 style="text-align=center">Hello {name}</h1>'
        "<p>This is a paragraph</p>"
        "<p>Another paragraph</p>"
    )


# Also possible
@app.route("/username/<name>/yessir")
def greetings(name):
    return f"Hello {name}"


# You can also specify the datatype of the argument
@app.route("/username/<name>/<int:number>")
def congratulate(name, number):
    return f"Congratulations {name} on your {number} birthday, next year you are {number +1} years old"


if __name__ == "__main__":
    app.run(debug=True)
