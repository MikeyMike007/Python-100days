import utils
from snake import Snake
from food import Food
from turtle import Screen
import time
from scoreboard import ScoreBoard


game_is_on = True

# Initialize screen
screen = Screen()
screen.screensize(utils.SCREEN_WIDTH, utils.SCREEN_LENGTH)
screen.bgcolor(utils.SCREEN_BG_COLOR)
screen.title(utils.SCREEN_TITLE)
screen.tracer(0)  # Make so that screen only updates on update()

# Make screen listen for keystrokes - Define actions when keys are pressed
screen.listen()
snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


food = Food()
scoreboard = ScoreBoard()

while game_is_on:
    time.sleep(utils.SLEEP_TIME)
    screen.update()
    snake.move()

    # Check for collisions between snake head and food
    if snake.head.distance(food) < utils.SNAKE_FOOD_COLLISION_TOLERANCE:
        scoreboard.add_score()
        snake.add_segment()
        food.move()

    # Check for collisions between snake head and game board
    if (
        snake.head.xcor() > utils.BOARD_SIDE
        or snake.head.xcor() < -utils.BOARD_SIDE
        or snake.head.ycor() > utils.BOARD_SIDE
        or snake.head.ycor() < -utils.BOARD_SIDE
    ):

        game_is_on = False
        scoreboard.game_over()

    # Check for collisions between snake head and snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < utils.HEAD_BODY_COLLISION_TOLERANCE:
            game_is_in = False
            scoreboard.game_over()


screen.exitonclick()
