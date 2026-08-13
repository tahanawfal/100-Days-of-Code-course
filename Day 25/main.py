import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./Day 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# extract csv
csv_path = "./Day 25/50_states.csv"
df = pd.read_csv(csv_path)

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    if answer_state in df['state'].values:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_guesses.append(answer_state)
        state_data = df[df['state'] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

for state in df['state'].values:
    with open("states_to_learn.txt", "a") as states_file:
        if state not in correct_guesses:
            states_file.write(f"{state}\n")

screen.mainloop()