from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
screen.setup(width=1000, height=1000)


# W = forward
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = clear drawing
speed = 10

def move_forwards():
    tim.forward(speed)

def move_backwards():
    tim.backward(speed)

def clockwise():
    tim.forward(speed)
    tim.right(speed)

def counter_clockwise():
    tim.backward(speed)
    tim.left(speed)

def clear_drawing():
    tim.home()
    tim.clear()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
