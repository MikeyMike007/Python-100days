# Day 18 - Turtle graphics, tuples and importing modules

## Understanding turtle graphics and how to use the documentation

[turtle — Turtle graphics — Python 3.9.1 documentation](https://docs.python.org/3/library/turtle.html)

[CS111 - Turtle Colors](https://cs111.wellesley.edu/labs/lab01/colors)

[Colors](https://trinket.io/docs/colors)

## Draw a square

```py
from turtle import Turtle, Screen

tim = Turtle()

tim.shape('turtle')
tim.color('red')

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
```

## Importing modules, installing packages and working with aliases

This can be done in many different ways, such as,

`from turtle import Turtle`

`from turtle import *`

`import turtle as t`

## Draw a dashed line

```py
from turtle import Turtle, Screen

tim = Turtle()
dash_length = 10
number_of_dashes = 10

for _ in range(number_of_dashes):
    tim.pendown()
    tim.forward(dash_length)
    tim.penup()
    tim.forward(dash_length)

screen = Screen()
screen.exitonclick()
```

## Drawing different shapes

```py
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
length = 100
tim.pendown()
max_corners = 10
min_corners = 3
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

for corners in range(min_corners, max_corners + 1):
    current_color = random.choice(colors)
    tim.pencolor(current_color)
    angle = 360 / corners
    for _ in range(corners):
        tim.right(angle)
        tim.forward(100)

screen.exitonclick()
```

## Generate a random walk

```py
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
angles = [0, 90, 180, 270]
step_length = 30
tim.pensize(20)
tim.speed("slow")
tim.pendown()

for _ in range(100):
    color = random.choice(colors)
    tim.pencolor(color)
    angle = random.choice(angles)
    tim.setheading(angle)
    tim.forward(step_length)

screen.exitonclick()
```

## Tuples

Main different between tuples and arrays is that tuples are immutable i.e. you
cannot change their values

```python
my_tuple = (1, 2, 3)
my_array = [1, 2, 3]
```

## Generate a random walk with random (r, g, b) colors

```py
import random
from turtle import Turtle, Screen, colormode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, b, g)
    return rand_color

tim = Turtle()
screen = Screen()
colormode(255)

angles = [0, 90, 180, 270]
step_length = 30
tim.pensize(20)
tim.speed("slow")
tim.pendown()

for _ in range(30):
    color = random_color()
    tim.pencolor(color)
    angle = random.choice(angles)
    tim.setheading(angle)
    tim.forward(step_length)

screen.exitonclick()
```

## Draw a spirograph

```py
import random
from turtle import Turtle, Screen, colormode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, b, g)
    return rand_color

tim = Turtle()
screen = Screen()
colormode(255)
tim.speed(('fastest'))

for angle in range(0, 360, 5):
    tim.setheading(angle)
    color = random_color()
    tim.pencolor(color)
    tim.circle(150)
    print(angle)

screen.exitonclick()
```

## Project - Damian Hirst

```py
import colorgram
import random
from turtle import Turtle, Screen, colormode


def draw_dot(timmy, color, x, y):
    timmy.goto(x, y)
    timmy.fillcolor(color)
    timmy.begin_fill()
    timmy.circle(10)
    timmy.end_fill()


colors = []
image_colors = colorgram.extract('dots.jpg', 20)

for color in image_colors:
    colors.append(color.rgb)


tim = Turtle()
screen = Screen()

tim.speed('fastest')
tim.penup()
tim.hideturtle()
colormode(255)

for x in range(-500, 500, 50):
    for y in range(-500, 500, 50):
        set_color = random.choice(colors)
        draw_dot(tim, set_color, x, y)

screen.exitonclick()
```

## Other

Recommended book: The stuffed shark

