from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
board = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_spd)
    screen.update()
    ball.move()
    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect right paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 322 or ball.distance(l_paddle) < 50 and ball.xcor() < -322:
        ball.bounce_x()
    # detect ball missing right paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        board.l_point()
    # detect ball missing left paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        board.r_point()

screen.exitonclick()



""" DONE -----
#TODO create screen
#TODO create and move paddle
#TODO create 2nd paddle
#TODO create ball, make it move
#TODO detect collision with wall
#TODO detect collision with paddle
#TODO detect paddle missing
#TODO keep score
#TODO speed up ball
"""
