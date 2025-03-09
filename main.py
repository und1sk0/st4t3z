import turtle
import pandas as pd
from board import Board
FONT = ("Times New Roman", 10, "Normal")

states = pd.read_csv("50_states.csv")
state_map = "blank_states_img.gif"
main_screen = turtle.Screen()
main_screen.title("US States Game")
main_screen.addshape(state_map)
turtle.shape(state_map)
state_board = Board()
counter = 0

while counter < 50:
    answer_state = main_screen.textinput(title="Guess the State", prompt="Enter a state name:")
    print(answer_state)
    match = tuple(states.loc[states["states"] == answer_state].iloc[0])
    state_board.place_state(match)

main_screen.exitonclick()
