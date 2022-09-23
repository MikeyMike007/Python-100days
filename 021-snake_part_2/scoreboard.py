from turtle import Turtle
import utils


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(utils.SCOREBOARD_COLOR)
        self.penup()
        self.goto(utils.SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"Current score: {self.score}"
        self.write(text, align=utils.SCOREBOARD_ALIGNEMENT, font=utils.SCOREBOARD_FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(utils.SCOREBOARD_GAME_OVER_POSITION)
        text = "Game over"
        self.write(
            text, align=utils.SCOREBOARD_ALIGNEMENT, font=utils.SCOREBOARD_FONT
        )
