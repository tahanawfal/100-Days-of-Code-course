from turtle import Turtle

ball_width = 20
ball_height = 20
x_start = 0
y_start = 0
ball_distance = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white") 
        self.penup()

    def move(self, x_dim, y_dim):
        if self.ycor() < (y_dim/2) and self.ycor() > (y_dim/-2):
            new_x = self.xcor() + 1
            new_y = self.ycor() + 1
            self.goto(new_x, new_y)
        else:


    def bounce_logic(self, y_dim):
        if self.ycor() < (y_dim/2) and self.ycor() > (y_dim/-2):
            ball_distance = 1 * ball_distance
        else:
            ball_distance = -1 * ball_distance