import turtle
from turtle import Screen, Turtle
import time
import random
from player import Player, Bullet
from scoreboard import ScoreBoard


player = Player()
bullet = Bullet()
score_board = ScoreBoard()


def fire_bullet():
    x_pos = player.xcor()
    y = player.ycor()
    bullet.setposition(x_pos, y + 30)
    bullet.showturtle()


screen = Screen()
screen.setup(width=540, height=540)
screen.bgcolor("lightgreen")
screen.title("Space Invaders")

border = Turtle()
border.speed(0)
border.penup()
border.color("black")
border.setposition(-200, -200)
border.pendown()
for n in range(4):
    border.forward(400)
    border.left(90)
border.hideturtle()


turtle.register_shape("images/alien.gif")

invader = Turtle()
invader.shape("images/alien.gif")
invader.penup()
invader.speed(0)
invader.setposition(-180, 180)


turtle.listen()
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
turtle.onkey(fire_bullet, "space")

bullet_speed = 10
invader_speed = 2

while True:
    screen.update()
    invader.forward(invader_speed)
    if invader.xcor() > 180 or invader.xcor() < -180:
        invader.right(180)
        invader.forward(invader_speed)
    bullet.forward(bullet_speed)

    if abs(bullet.xcor() - invader.xcor()) < 15 and abs(bullet.ycor() - invader.ycor()) < 15:
        score_board.track_score()

        bullet.hideturtle()
        invader.hideturtle()
        time.sleep(1)

        invader.showturtle()
        x = random.randint(-180, 180)
        invader.setposition(x, 180)

