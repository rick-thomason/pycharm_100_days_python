import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

# Canvas
canvas = tk.Canvas(height=200, width=200)
image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.pack()

window.mainloop()