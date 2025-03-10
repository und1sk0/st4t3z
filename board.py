from turtle import Turtle

FONT = ("Courier New", 8, "bold")


class Board(Turtle):

    def __init__(self, state_data):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.state_data = state_data
        self.place_state()

    def place_state(self):
        print(self.state_data)
        self.goto((self.state_data["x"], self.state_data["y"]))
        self.write(
            self.state_data["state"],
            align="center",
            font=FONT,
        )
