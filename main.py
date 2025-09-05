import turtle
import pandas as pd
from board import Board

states_img = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(states_img)
turtle.shape(states_img)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses = []
correct_guesses = []

while len(guesses) < 50:
    guess = screen.textinput(
        title=f"Guess a state {len(guesses)}/50",
        prompt="Enter state name: "
    ).title()

    if guess == "Exit":
        states_not_guessed = [state for state in all_states if state not in guesses]
        print(states_not_guessed)
        states_to_learn = pd.DataFrame(states_not_guessed)
        states_to_learn.to_csv(("states_to_learn.csv"))
        break

    if guess in all_states:
        guesses.append(guess)
        x, y = data.loc[data["state"] == guess, ["x", "y"]].iloc[0]
        correct_guesses.append(guess)
        put_state = Board(x, y, guess)

screen.exitonclick()