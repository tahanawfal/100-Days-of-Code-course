from turtle import Turtle

ball_width = 20
ball_height = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white") 
        self.penup()
        self.move_speed = 0.01
        self.x_diraction = 1
        self.y_diraction = 1

    def move(self):
        new_x = self.xcor() + self.x_diraction
        new_y = self.ycor() + self.y_diraction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_diraction *= -1
            
    def bounce_x(self):
        self.x_diraction *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto((0,0))
        self.bounce_x()
        self.move_speed = 0.01