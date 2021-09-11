from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    """docstring for ScoreBoard."""

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            num = data.read()
        self.score = 0
        self.high_score = int(num)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
