from turtle import Turtle
STARTING_POS =[(0, 0), (-20, 0), (-40, 0)]
MOVING_DIST = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake():

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for pos in STARTING_POS:
            """creating 3 starting segments"""
            self.add_segment(pos)

    def add_segment(self, pos):
        snake = Turtle('square')
        snake.color('chartreuse3')
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.fd(MOVING_DIST)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
