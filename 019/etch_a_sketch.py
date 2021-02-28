from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_fd():
    tim.fd(10)

def move_bk():
    tim.bk(10)

def turn_l():
    tim.left(10)

def turn_r():
    tim.right(10)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key ='w', fun = move_fd)
screen.onkey(key ='s', fun = move_bk)
screen.onkey(key ='a', fun = turn_l)
screen.onkey(key ='d', fun = turn_r)
screen.onkey(key ='c', fun = clear)

screen.exitonclick()
