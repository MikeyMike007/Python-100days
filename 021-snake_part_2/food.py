from turtle import Turtle
import random
import utils


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(utils.FOOD_SHAPE)
        self.color(utils.FOOD_COLOR)
        self.penup() # If you dont pull up pen it will paint a path when you call goto()
        self.position = self.generate_position()
        self.goto(self.position)

    def generate_position(self):
        x_cor = random.randint(-utils.BOARD_SIDE, utils.BOARD_SIDE)
        y_cor = random.randint(-utils.BOARD_SIDE, utils.BOARD_SIDE)
        return (x_cor, y_cor)

    def move(self):
        self.clear()
        self.position = self.generate_position()
        self.goto(self.position)
