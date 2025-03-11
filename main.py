import turtle
import pandas as pd
from board import Board

states = pd.read_csv("50_states.csv")
state_map = "blank_states_img.gif"
main_screen = turtle.Screen()
main_screen.title("US States Game")
main_screen.addshape(state_map)
turtle.shape(state_map)
states_to_learn = pd.DataFrame(columns=["state", "x", "y"])
guesses = []
missed = []

while len(guesses) < 51:
    try:
        answer_state = main_screen.textinput(
            title=f"Score {len(guesses)}/50", prompt="Enter state name:"
        ).title()
    except AttributeError:
        break

    if answer_state in states.state.tolist():
        print(answer_state)
        match = states.loc[states["state"] == answer_state].iloc[0]
        state = Board(match)
        guesses.append(answer_state)

states_to_learn = [ state for state in states.state.tolist() if state not in guesses ]
states_to_learn_df = pd.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")
main_screen.exitonclick()
