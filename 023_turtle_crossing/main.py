import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkGrey')
screen.tracer(0)
screen.title('Turtle Crossing')

turt = Player()
board = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(turt.move, 'Up')


def game():
    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        # create car every 0.1s
        car_manager.create()
        car_manager.move()
        # detect finish line and increase level
        if turt.finish_line():
            board.increase_level()
            turt.reset_pos()
            car_manager.increase_speed()
        # detect collision and end game
        for car in car_manager.all_cars:
            if car.distance(turt) < 20:
                game_on = False
                board.game_over()

game()

screen.exitonclick()

""" ---DONE
#TODO create scoreboard
#TODO create player & make move
#TODO create car
#TODO make car move
#TODO detect level end & reset player
#TODO increase level speed
"""
