from turtle import Turtle

MOVING_DIST = 5
BALL_SPD = 0.05


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = MOVING_DIST
        self.y_move = MOVING_DIST
        self.move_spd = BALL_SPD

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_spd *= 0.9

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_spd = BALL_SPD
