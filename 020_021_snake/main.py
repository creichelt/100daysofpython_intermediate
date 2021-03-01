from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

def game():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            board.increase_score()
        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            board.reset()
            snake.reset()
        # Detect collision with self
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                board.reset()
                snake.reset()

game()

screen.exitonclick()



# with open('save.txt', mode ='w') as file:
# #    contents = file.read()
# #    print(contents)
#     file.write('new text bla')
