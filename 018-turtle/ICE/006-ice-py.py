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


