import turtle as t
import pandas

screen = t.Screen()
screen.title("USA States Game")
image_path = "data/blank_states_img.gif"
screen.addshape(image_path)
t.shape(image_path)

score = 0;
correct_guesses = set()
states_to_learn = []
data = pandas.read_csv("data/50_states.csv")
all_states = set(data.state.to_list())
writter = t.Turtle()
writter.hideturtle()

while len(correct_guesses) < 50:
    answer_state = t.textinput(title="{}/50 guessed".format(score), prompt="What's another state's name?").title()
    guessed_state = data[data["state"] == answer_state.title()]
    #if guessed_state.state.T.item() != None :

    if answer_state == "Exit":
        [states_to_learn.append(state) for state in all_states.difference(correct_guesses)]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break;
        
    if answer_state in correct_guesses:
        continue

    if answer_state in all_states:
        score += 1
        # x_cor = guessed_state["x"].item()
        # y_cor = guessed_state["y"].item()
        writter.penup()
        # writter.goto(x_cor,y_cor)
        writter.goto(int(guessed_state.x), int(guessed_state.y))
        writter.pendown()
        writter.write(guessed_state.state.item())
        correct_guesses.add(guessed_state.state.item())




