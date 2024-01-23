from turtle import Turtle
import turtle


MOVING_DISTANCE = 15
turtle.register_shape("images/rocket.gif")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/rocket.gif")
        self.penup()
        self.speed("fastest")
        self.setposition(0, -180)

    def move_left(self):
        x = self.xcor() - MOVING_DISTANCE
        if x < -190:
            x = -190
        self.setx(x)

    def move_right(self):
        x = self.xcor() + MOVING_DISTANCE
        if x > 190:
            x = 190
        self.setx(x)


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(.5,.5)
        self.hideturtle()



