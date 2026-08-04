from turtle import Turtle

paddle_width = 20
paddle_length = 100
distance_move = 20

class Paddle:
    def __init__(self):
        self.x_position = 350
        self.y_position = 0
        self.create_paddle()

    def create_paddle(self):
        paddle_piece = Turtle(shape="square")
        paddle_piece.shapesize(stretch_wid=5, stretch_len=1) 
        paddle_piece.color("white")
        paddle_piece.penup()
        paddle_piece.goto((self.x_position, self.y_position))

    def up(self):
        self.paddle_piece.color("red")

    def down(self):
        self.paddle_piece.goto(self.paddle_piece.xcor(), self.paddle_piece.ycor() - distance_move)