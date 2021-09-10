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

player = Player()
car_manager = CarManager()

screen.onkey(player.go_up, "Up")

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # detect if player made it across
    if player.is_at_finish_line():
        player.goto_start()
        score.level += 1
        score.update_scoreboard()

screen.exitonclick()
