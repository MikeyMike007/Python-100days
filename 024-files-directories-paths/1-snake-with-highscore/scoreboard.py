from turtle import Turtle
import utils


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.color(utils.SCOREBOARD_COLOR)
        self.penup()
        self.goto(utils.SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"Current score: {self.score} - High score: {self.high_score}"
        self.write(text, align=utils.SCOREBOARD_ALIGNEMENT, font=utils.SCOREBOARD_FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_highscore(self):
        with open(utils.HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def read_highscore(self):
        with open(utils.HIGH_SCORE_FILE) as file:
            return int(file.read())

    # def game_over(self):
    #     self.goto(utils.SCOREBOARD_GAME_OVER_POSITION)
    #     text = "Game over"
    #     self.write(text, align=utils.SCOREBOARD_ALIGNEMENT, font=utils.SCOREBOARD_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
