from turtle import Screen, Turtle
from snake_body import SnakeBody


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
tim = Turtle()

def make_snake_body(num):
    count = 0
    while count < num:
        tim.pendown()
        new_body = SnakeBody()
        tim.color(new_body.color)
        tim.begin_fill()
        tim.backward(new_body.width)
        tim.right(90)
        tim.forward(new_body.width)
        tim.left(90)
        tim.forward(new_body.height)
        tim.left(90)
        tim.forward(new_body.width)
        tim.end_fill()
        tim.penup()
        tim.right(90)
        tim.backward(new_body.width)
        count += 1






make_snake_body(4)


screen.exitonclick()
