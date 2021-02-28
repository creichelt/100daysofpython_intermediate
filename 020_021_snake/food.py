from turtle import Turtle
import random
# import main


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('DeepPink3')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)