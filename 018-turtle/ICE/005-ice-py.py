# Generate a random walk with random (r, g, b) colors
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
