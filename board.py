from turtle import Turtle
FONT = ("Courier New", 6, "bold")


class Board(Turtle):

    def __init__(self, x, y, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.x = x
        self.y = y
        self.state = state
        self.place_state()

    def place_state(self):
        self.goto((self.x, self.y))
        self.write(
            self.state,
            align="center",
            font=FONT,
        )