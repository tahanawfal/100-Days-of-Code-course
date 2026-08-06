from turtle import Turtle

paddle_width = 20
paddle_length = 100
distance_move = 20

class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) 
        self.penup()
        self.goto((x_position, y_position))

    def up(self):
        self.goto(self.xcor(), self.ycor() + distance_move)

    def down(self):
        self.goto(self.xcor(), self.ycor() - distance_move)