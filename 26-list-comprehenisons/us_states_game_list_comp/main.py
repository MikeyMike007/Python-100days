import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"

# Code to use an image as turtle's shape
screen.addshape(image)
turtle.shape(image)

# Read in csv file to DataFrame
data = pandas.read_csv("./50_states.csv")

# Extract all states
all_states = data["state"].to_list()

guessed_states = []

# Run while you have not guessed all states
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / 50 states correct",
        prompt="Whats another states name?",
    ).title()

    # Code to run if you want to exit
    # It basically will print out all the unguessed states
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        for state in missing_states:
            print(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Code to run if a guess is correct
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Extract x and y coordinates
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)  # to get the row value: state_data["state"].item()


def get_mouse_click_coor(x, y):
    print(x, y)


# Function to be run if you click on the screen
turtle.onscreenclick(get_mouse_click_coor)
