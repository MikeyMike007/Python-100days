# Generate a random walk
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
