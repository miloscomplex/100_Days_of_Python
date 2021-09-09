import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_NUM = 10;
cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("LightGray")
screen.listen()

for i in range(CAR_NUM):
    car = CarManager()
    cars.append(car)

player = Player()

screen.onkey(player.go_up, "Up")

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    for car in cars:
        car.move_forward()

    screen.update()
