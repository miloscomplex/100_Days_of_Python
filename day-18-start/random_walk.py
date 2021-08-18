from turtle import Screen
import turtle as t
import random
from random import randrange

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("coral")
tim.pensize(10)
tim.speed("fastest")

colors = ["cornflower blue","forest green","dark salmon","medium purple","magenta","wheat"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

print(random_color())

directions = [0, 90, 180, 270]

for _ in range(300):
    tim.color(random_color())
    tim.forward(30 + random.randint(0, 30))
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
