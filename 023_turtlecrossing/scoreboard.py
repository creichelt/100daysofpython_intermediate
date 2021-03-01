from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-285, 270)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align='center')