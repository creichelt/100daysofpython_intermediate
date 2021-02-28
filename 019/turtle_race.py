from turtle import Turtle,Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet",
                       prompt="Which turtle will win the race? Enter a color "
                              "('red', 'blue', 'grey', 'green', 'pink', 'coral'): ")

colors = ['red', 'blue', 'grey', 'green', 'pink', 'coral']
all_turtles = []

for i in range(len(colors)):
    """creating new turtles"""
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,(i*40)-90)
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            race_on = False
            winner = i.pencolor()
            if winner == bet:
                print(f"You've won.")
            else:
                print(f"You've lost.")
            print(f"Winning color is {winner}")

        rand_distance = random.randint(0,10)
        i.fd(rand_distance)

screen.exitonclick()