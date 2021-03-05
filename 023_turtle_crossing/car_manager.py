from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_spd = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            # having cars drive in lanes rather than completely random
            # lanes = []
            # for i in range(-250, 250, 20):
            #     lanes.append(i)
            # pos = random.choice(lanes)
            pos = random.randint(-250, 250)
            car.goto(300, pos)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.bk(self.car_spd)

    def increase_speed(self):
        self.car_spd += MOVE_INCREMENT

