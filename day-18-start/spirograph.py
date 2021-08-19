from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.pensize(3)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

directions = [0, 90, 180, 270]

heading = 0
for n in range(0, 365, 5):
    tim.color(random_color())
    tim.circle(200)
    tim.setheading(n)
    # heading += 5

screen = Screen()
screen.exitonclick()
