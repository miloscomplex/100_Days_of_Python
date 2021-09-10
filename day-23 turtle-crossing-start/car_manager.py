import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TOP_MAX = 250
BOTTOM_MAX = -250


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(random.randint(300, 690), random.randint(BOTTOM_MAX, TOP_MAX))


    def move_forward(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
        if self.xcor() < -350:
            self.goto(300, random.randint(BOTTOM_MAX, TOP_MAX))
            self.color(COLORS[random.randint(0, len(COLORS) - 1)])
