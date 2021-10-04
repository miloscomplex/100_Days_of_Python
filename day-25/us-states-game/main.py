import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

def correct_guess(guess):
    if states_data[states_data.state == guess.title()]:
        print("yup")
    else:
        print(guess)


correct_guess(answer_state)

turtle.mainloop()
