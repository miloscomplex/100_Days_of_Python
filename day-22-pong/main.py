import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "z")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #detect collision with r_paddle or l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect if r_paddle missed
    if ball.xcor() > 390:
        scoreboard.l_point()
        time.sleep(0.1)
        ball.reset_position()

    #Detect if l_paddle missed
    if ball.xcor() < -390:
        scoreboard.r_point()
        time.sleep(0.1)
        ball.reset_position()

    #detect collision with l_paddle

screen.exitonclick()
