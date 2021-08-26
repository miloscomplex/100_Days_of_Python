from turtle import Turtle, Screen
import random


# tim = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# W = forward

colors = ["red","orange","yellow","green","blue","indigo","violet"]
all_turtles = []

x_pos = -235
y_pos = -100

def createTurtle(turtle_color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    global x_pos, y_pos
    new_turtle.goto(x= x_pos, y= y_pos)
    y_pos += 30
    all_turtles.append(new_turtle)

for color in colors:
    createTurtle(color)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
