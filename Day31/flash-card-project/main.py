import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except (FileNotFoundError, ValueError):
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# function to call next card when button is clicked
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file='images/card_front.png')
card_back_image = tk.PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=('Arial', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, font=('Arial', 60, 'bold'), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(columnspan=2, column=0, row=0)

# Buttons
wrong_image = tk.PhotoImage(file='images/wrong.png')
unknown_button = tk.Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)

correct_image = tk.PhotoImage(file='images/right.png')
known_button = tk.Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()



