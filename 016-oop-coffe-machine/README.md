# Object oriented programming

```python
# Just an example - code will not work
# Blueprint for a waitreess
class Waitress:
    # Attributes - i.e. What the waitress has
    is_holding_plates = True
    tables_responsible = [1, 2, 3]

    # Methods - i.e. What the waitress can do

    # Takes orders
    def take_order(table, order):

    # Takes payments
    def take_payment(amount):


# You can then create an object from the blueprint i.e.

anna = Waitress()
```

## Introduction to Turtle

```py
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
```

Turtle documentation: [turtle — Turtle graphics — Python 3.9.1 documentation](https://docs.python.org/3/library/turtle.html) \
Turtle colors: [CS111 - Turtle Colors](https://cs111.wellesley.edu/labs/lab01/colors)

## How to add python packages and Pypi

`pip add package_name`

## PrettyTable

```py
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
```
