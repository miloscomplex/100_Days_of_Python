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
    tim.clear()
    tim.pendup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
