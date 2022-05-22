import tkinter as tk
import pandas as pd
import random

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
print(to_learn)


# function to call next card when button is clicked
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])


BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file='images/card_front.png')
card_back_image = tk.PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(columnspan=2, column=0, row=0)

# Buttons
wrong_image = tk.PhotoImage(file='images/wrong.png')
wrong_button = tk.Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

correct_image = tk.PhotoImage(file='images/right.png')
correct_button = tk.Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()



