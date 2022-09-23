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
