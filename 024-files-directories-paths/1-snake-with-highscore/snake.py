from turtle import Turtle
import utils


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake(self):
        for position in utils.SNAKE_INITIAL_POSITIONS:
            segment = Turtle()
            segment.color(utils.SNAKE_COLOR)
            segment.shape(utils.SNAKE_SHAPE)
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.color(utils.SNAKE_COLOR)
        new_segment.shape(utils.SNAKE_SHAPE)
        new_segment.penup()
        new_xcor = self.segments[-1].xcor()
        new_ycor = self.segments[-1].ycor()
        new_segment.goto((new_xcor, new_ycor))
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.initialize_snake()
        self.head = self.segments[0]

    def move(self):
        for position_nr in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[position_nr - 1].xcor()
            new_ycor = self.segments[position_nr - 1].ycor()
            self.segments[position_nr].goto((new_xcor, new_ycor))

        self.head.forward(utils.SNAKE_STEP_SIZE)

    def up(self):
        if self.head.heading() != utils.DOWN:
            self.head.setheading(utils.UP)

    def down(self):
        if self.head.heading() != utils.UP:
            self.head.setheading(utils.DOWN)

    def right(self):
        if self.head.heading() != utils.LEFT:
            self.head.setheading(utils.RIGHT)

    def left(self):
        if self.head.heading() != utils.RIGHT:
            self.head.setheading(utils.LEFT)
