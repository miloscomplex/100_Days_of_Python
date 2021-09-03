from turtle import Turtle
SPEED = 20

class Paddle:
    """docstring for paddle."""

    def __init__(self):
        self.create_paddle()

    def create_paddle(self):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.shapesize(20,100)
        new_paddle.penup()
        new_paddle.goto(350, 0)

    def up(self):
        pass
