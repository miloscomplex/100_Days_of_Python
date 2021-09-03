from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Pong")


paddle = Paddle()
paddle.up()


screen.exitonclick()
