from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("Name the States")
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answer_list = []

state_data = pandas.read_csv("50_states.csv")
state_names = state_data["state"]
states_list = state_names.to_list()

def take_input():
    answer = screen.textinput(f"{len(correct_answer_list)}/50 States correct", "What's another state's name?")
    answer = answer.title()
    return answer


def write_state_name(answer, x, y):
    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(x, y)
    timmy.write(answer, align="center", font=("Courier", 10, "normal"))


game_is_on = True
while game_is_on:
    ans = take_input()
    guessed_list = [state_name for state_name in states_list if ans == state_name and ans not in correct_answer_list]
    correct_answer_list.extend(guessed_list)
    states_list = [state_name for state_name in states_list if state_name != ans]
    if ans in correct_answer_list:
        state_row = state_data[state_data.state == ans]
        state_x = state_row.x
        write_state_name(ans, int(state_x), int(state_row.y))
    if ans == 'Q' or len(correct_answer_list) == 50:
        game_is_on = False
        break

state_dict = {
    "Missed State names": states_list
}

missed_state = pandas.DataFrame(state_dict)
missed_state.to_csv("Missed_State.csv")
# print(answer)
# def click_on_screen_cor(x, y):
#     print(x, y)
# screen.onclick(click_on_screen_cor)

# screen.mainloop() is used to avoid the main screen to be closed ever after executing all the codes.
