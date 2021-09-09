import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TOP_MAX = -270
BOTTOM_MAX = 270


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(random.randint(-290, 290), random.randint(-270, 270))


    def move_forward(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
        if self.xcor() < -350:
            self.goto(300, random.randint(-270, 270))
            self.color(COLORS[random.randint(0, len(COLORS) - 1)])
