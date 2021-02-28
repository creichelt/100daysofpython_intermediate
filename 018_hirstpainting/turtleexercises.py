from turtle import Turtle, Screen
import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('red')

""" make turtle turn """
# for i in range(4):
#     timmy.fd(100)
#     timmy.right(90)

""" create a dashed line """
# for i in range(10):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()


import random

colors = ['red', 'blue', 'orange', 'pink', 'green', 'black', 'coral']

""" drawing shapes from triangle to decagon using only loops"""
# n = 2
# for shapes in range(len(colors)):
#     timmy.color(random.choice(colors))
#     n += 1
#     for i in range (n):
#         timmy.fd(100)
#         timmy.right(360/n)

""" drawing shapes from triangle to decagon using a function and a loop"""
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range (num_sides):
#         timmy.fd(100)
#         timmy.right(angle)
#
# for shape_sides_n in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_sides_n)

direction = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    """ generating a random rgb color """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def walk():
    """ sending the turtle on a random walk"""
    timmy.pensize(15)
    timmy.speed('fastest')
    timmy.fd(30)
    timmy.color(random_color())
    timmy.setheading(random.choice(direction))

# for i in range(200):
#     walk()

def spirograph(gap_size):
    """ drawing a spirograph"""
    for i in range(int(360/gap_size)):
        timmy.circle(40)
        timmy.speed('fastest')
        timmy.color(random_color())
        timmy.setheading(timmy.heading()+gap_size)

# spirograph(10)



screen = Screen()
screen.exitonclick()
