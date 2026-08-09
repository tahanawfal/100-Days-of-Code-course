from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = f"Level: {self.level}"
        self.show_level()

    def show_level(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.write(self.score, align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.show_level()

    def game_over(self):
        print("meow")