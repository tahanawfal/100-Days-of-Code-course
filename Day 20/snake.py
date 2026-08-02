from turtle import Turtle

move_distance = 20
block_length = 20
start_position = [0,0]
start_positions = [ (start_position[0], start_position[1] ),
( (-1 * block_length) + start_position[0], start_position[1] ),
( (-2 * block_length) + start_position[0], start_position[1] ) ]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in start_positions:
            seg_block = Turtle(shape="square")
            seg_block.color("white")
            seg_block.penup()
            seg_block.goto(position)
            self.segments.append(seg_block)

    def move(self):
        for seg_block in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_block - 1].xcor()
            new_y = self.segments[seg_block - 1].ycor()
            self.segments[seg_block].goto(new_x, new_y)
            self.segments[0].forward(move_distance)