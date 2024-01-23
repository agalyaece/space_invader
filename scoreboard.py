from turtle import Turtle

FONT = ("courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-200, 210)
        self.speed("fastest")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}", align="left", font=FONT)

    def track_score(self):
        self.score += 1
        self.update_score()


