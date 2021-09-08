import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SPEED = 10;
CAR_NUM = 20;
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

def go_up():
    turtle.forward(SPEED)

turtle = Turtle()
turtle.penup()
turtle.shape("turtle")
turtle.left(90)
turtle.goto(0,-280)

screen.listen()
screen.onkey(go_up, "Up")

for i in range(CAR_NUM):
    car = CarManager()
    cars.append(car)

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    for car in cars:
        car.move_forward()

    screen.update()
