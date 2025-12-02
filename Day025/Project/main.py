import turtle
import pandas

'''Setting up the Screen'''
my_screen = turtle.Screen()
my_screen.title("India States Game")
image = "India_Map.gif"
my_screen.addshape(image)  # Register the GIF image as a new turtle shape
turtle.shape(image)  # Set the turtle’s appearance to the map image

'''Reading the csv file which contains all the states and it's coordinates according to the gif
image of India Map'''
data = pandas.read_csv("states.csv")
all_states = data.state.to_list()  # Converting all state names into list


'''The commented out code is used to get the coordinates of particular location where ever 
we have clicked'''
# def get_mouse_click_corr(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_corr)

guessed_states = []
while len(guessed_states) < 30:
    answer_state = my_screen.textinput(title=f"{len(guessed_states)}/30 states correct", prompt="Type the name of the state in India").title()

    '''If the input is 'Exit' then the programs creates a csv file which consists of the states
    which i am unable to guess or missed, so you can learn'''
    states_to_learn = []
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        missing_states = pandas.DataFrame(states_to_learn)
        missing_states.to_csv("States_to_learn.csv")
        break

    '''If the answer state is in the all_states list then the name of that state is printed at the
    respected coordinates of that state'''
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


my_screen.mainloop()
