import random
from turtle import Screen
import turtle as t

color_list = [(1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63), (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20), (175, 134, 162), (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85)]

tim = t.Turtle()
# change to rgb tuttle mode
t.colormode(255)
# tim.goto(200, 1000)

tim.shape("turtle")
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(600)
tim.setheading(0)

def random_color():
    random_int = random.randint(0, len(color_list) - 1)
    return color_list[random_int]

def draw_line_of_circles():
    for n in range(0, 110, 10):
        tim.dot(20, random_color())
        tim.forward(50)


x = round(tim.xcor())
y = round(tim.ycor())

for _ in range(10):
    tim.setpos(x,y)
    draw_line_of_circles()
    y += 40
    

screen = Screen()
screen.exitonclick()
