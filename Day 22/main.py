import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen_width = 800
screen_height = 600

upper_wall = (screen_height/2) - 20
lower_wall = upper_wall * -1

right_wall = (screen_width/2) - 20
left_wall = right_wall * -1

r_paddle_xcor = (screen_width/2) - 50
l_paddle_xcor = r_paddle_xcor * -1

r_paddle_edge = r_paddle_xcor - 20
l_paddle_edge = r_paddle_edge * -1



screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_width, height=screen_height)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(r_paddle_xcor, 0)
l_paddle = Paddle(l_paddle_xcor, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collistion with wall
    if ball.ycor() == upper_wall or ball.ycor() == lower_wall:
        ball.bounce_y()

    # Detect collisition with paddle
    if ball.xcor() > r_paddle_edge and ball.distance(r_paddle) < 50 or ball.xcor() < l_paddle_edge and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    # Detect right paddle misses the ball
    if ball.xcor() > right_wall:
        scoreboard.l_point()
        ball.reset_position()
    
    # Detect left paddle misses the ball
    if ball.xcor() < left_wall:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()