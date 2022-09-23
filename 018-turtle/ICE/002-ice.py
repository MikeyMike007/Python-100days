# Draw a dashed line
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
