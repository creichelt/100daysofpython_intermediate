""" retrieving the colors for color_list"""
# import colorgram
# colors = colorgram.extract('hirst.jpg',30)
# rgb = []
#
# for color in colors:
#     r =color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
#
# print(rgb)

from turtle import Turtle, Screen
import turtle as t
import random

color_list = [(234, 166, 59), (46, 112, 157),  (113, 150, 203),  (212, 123, 164), (17, 128, 96),
               (171, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (224, 76, 115),
               (163, 166, 35), (28, 35, 83), (228, 87, 43), (42, 166, 208), (119, 172, 116),
               (119, 102, 158), (215, 64, 33), (40, 53, 99), (75, 22, 45),
               (227, 171, 189), (19, 95, 70), (31, 62, 55), (13, 88, 104), (160, 208, 197),
               (180, 188, 209), (224, 177, 167)]

t.colormode(255)

turt = Turtle()
turt.speed('fastest')

turt.setheading(225)
turt.hideturtle()
turt.penup()
turt.fd(250)
turt.setheading(0)

number_dots = 100

for i in range(1,number_dots+1):
    turt.dot(20, random.choice(color_list))
    turt.penup()
    turt.fd(50)
    if i % 10 == 0:
        turt.penup()
        turt.setheading(90)
        turt.fd(50)
        turt.setheading(180)
        turt.fd(500)
        turt.setheading(0)
turt.hideturtle()

screen = Screen()
screen.exitonclick()
