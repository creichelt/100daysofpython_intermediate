from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('DarkOliveGreen')
        self.penup()
        self.speed('fast')
        self.setheading(90)
        self.reset_pos()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def reset_pos(self):
        self.goto(STARTING_POSITION)