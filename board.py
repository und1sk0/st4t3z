from turtle import Turtle
import pandas as pd

FONT = ("Courier New", 16, "bold")


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0

    def place_state(self, state_data):
        print(state_data)
        self.goto(state_data[1],state_data[2])
        self.write(
            state_data[0],
            align="center",
            font=FONT,
        )