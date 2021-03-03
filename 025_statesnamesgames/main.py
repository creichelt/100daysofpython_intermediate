import pandas as pd
import turtle as t
import csv

df = pd.read_csv('50_states.csv')
screen = t.Screen()
screen.setup(height=550, width=750)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

correct_states = []
usa = df.state.to_list()

while len(correct_states) <= 50:
    # done if all are entered
    if len(correct_states) == 50:
        print('You got them all!')
        break
    # ask user for a state
    answer = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?").title()
    state_df = df[df.state == answer]
    if answer == 'Exit':
        missing = list(set(usa) - set(correct_states))
        # creating output with missed states
        new_df = pd.DataFrame(missing)
        new_df.to_csv('Missing_states.csv')
        break
    if answer in usa:
        if answer not in correct_states:
            marker = t.Turtle()
            marker.hideturtle()
            marker.penup()
            marker.goto(int(state_df.x), int(state_df.y))
            marker.write(answer)
            correct_states.append(answer)







t.mainloop()




