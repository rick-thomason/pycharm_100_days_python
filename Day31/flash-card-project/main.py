import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file='images/card_front.png')
card_back_image = tk.PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(columnspan=2, column=0, row=0)

# Labels


# Buttons
wrong_image = tk.PhotoImage(file='images/wrong.png')
correct_image = tk.PhotoImage(file='images/right.png')

wrong_button = tk.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
correct_button = tk.Button(image=correct_image, highlightthickness=0)
correct_button.grid(column=1, row=1)






window.mainloop()



