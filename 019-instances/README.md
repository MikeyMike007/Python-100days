# Instances, state and higher order functions

## Python higher order functions and event listeners

Example of the higher order function `calculator()`:

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(1, 1, add)

# Prints 2
print(result)

```

## Make an Etch-A-Sketch App

```python
from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_counter_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

```

## Object state and instances

```python
# tommy and timmy are objects / instances
tommy = Turtle()
timmy = Turtle()

```

