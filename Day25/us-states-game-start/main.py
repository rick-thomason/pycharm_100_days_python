import pandas as pd
import turtle

states = pd.read_csv('50_states.csv')
image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(image)

turtle.shape(image)

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess The State',
                                    prompt='What"s another state"s name?').title().strip()

    if answer_state == 'Exit':
        missing_states = []
        for state in states['state']:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')
        break

    for state in states['state']:
        if answer_state == state:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states[states['state'] == answer_state]
            t.goto(int(state_data['x']), int(state_data['y']))
            t.write(answer_state)


