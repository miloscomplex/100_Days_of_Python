from turtle import Screen
import turtle as t
import random
from random import randrange

tim = t.Turtle()
tim.shape("turtle")
tim.color("coral")
tim.pensize(10)
tim.speed("fastest")

colors = ["cornflower blue","forest green","dark salmon","medium purple","magenta","wheat"]

directions = [0, 90, 180, 270]

for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(30 + randrange(20))
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
