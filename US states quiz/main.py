import turtle, pandas as pd

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
missing_states = []
while len(guessed_state)<50:
    ans_state = screen.textinput(title=f"{len(guessed_state)}/50 states guessed", prompt="Type the state").title()
    if ans_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if ans_state in all_states:
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates = data[data.state == ans_state]
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(ans_state)


screen.exitonclick()
