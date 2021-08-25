from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
screen.setup(width=500, height=500)

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()
