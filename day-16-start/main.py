# import turtle
# timmy = turtle.Turtle()

from prettytable import PrettyTable
table = PrettyTable();

from turtle import Turtle, Screen

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
print(timmy)

print(table)

my_screen  = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
