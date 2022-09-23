# Learnings

## Flask

### HTML decorators

```python
# HTML decorator that makes text bold
def make_bold(function):
    def bold_wrapper(*args, **kwargs):
        return f"<b>{function(*args)}</b>"

    return bold_wrapper

@make_bold
def greet(firstname, surname):
    return f"Hello {firstname} {surname}"

@make_bold
def greet_again(firstname):
    return f"Hello {firstname} again"

print(greet("Firstname", "Surname"))
print(greet_again("Firstname"))
```

### Guess the number game

```python
from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/")
def welcome():
    return """
        <h1>Guess a number between 0-9</h1>
        <p>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
        </p>
    """

@app.route("/<int:guess>")
def compare(guess):
    if guess > number:
        return """
        <h1>You guessed to high</h1>
        <p>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
        </p>
    """
    elif guess < number:
        return """
        <h1>You guessed to low</h1>
        <p>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
        </p>
    """
    else:
        return """
        <h1>You guessed the right number</h1>
        <p>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
    """

if __name__ == "__main__":
    app.run(debug=True)
```

### Routing Examples

```python
from flask import Flask

# Initiate app
app = Flask(__name__)

# Get argument name and pass that into function
@app.route("/username/<name>")
def greet(name):
    return (
        f'<h1 style="text-align=center">Hello {name}</h1>'
        "<p>This is a paragraph</p>"
        "<p>Another paragraph</p>"
    )

# Get argument name and pass that into the function below - Another variant
@app.route("/username/<name>/yessir")
def greetings(name):
    return f"Hello {name}"

# You can can also pass two different variables. Here, name is a str and number is an int.
# Note that you can in this way specify the type of the variable in the GET request
@app.route("/username/<name>/<int:number>")
def congratulate(name, number):
    return f"Congratulations {name} on your {number} birthday, next year you are {number +1} years old"

if __name__ == "__main__":
    app.run(debug=True)
```

### Example how you can use decorators to check if users are logged in

```python
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# We now want to decorate our function so that only users that are logged in
# can create a blogpost
def is_authenticated(func):
    def wrapper(*args, **kwargs):
        # if user.is_logged_in == True: # Doesnt work
        if args[0].is_logged_in is True:
            func(args[0])
        else:
            print(f"User {args[0].name} is not logged in. Cannot make blogpost.")

    return wrapper

@is_authenticated
def creat_blog_post(user):
    print(f"This is {user.name} blog post")

new_user = User("Angela")
creat_blog_post(new_user) # Not allowed to make a blog post

new_user.is_logged_in = True
creat_blog_post(new_user)  # Is allowed to make a blog post
```
