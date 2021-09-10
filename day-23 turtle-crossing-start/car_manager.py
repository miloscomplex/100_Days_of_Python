import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TOP_MAX = 250
BOTTOM_MAX = -250
LEFT_DISTANCE = -320


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        random_y = random.randint(BOTTOM_MAX, TOP_MAX)
        random_x = random.randint(300, 890)
        new_car.goto(random_x, random_y)
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < LEFT_DISTANCE:
                random_y = random.randint(BOTTOM_MAX, TOP_MAX)
                random_x = random.randint(300, 890)
                car.goto(random_x, random_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
