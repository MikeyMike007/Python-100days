# Drawing different shapes
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


