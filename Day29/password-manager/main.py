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
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text='Website:', fg='black')
website_label.grid(column=0, row=1)

email_username_label = tk.Label(text='Email/Username:', fg='black')
email_username_label.grid(column=0, row=2)

password_label = tk.Label(text='Password:', fg='black')
password_label.grid(column=0, row=3)

# Inputs
website_input = tk.Entry(bg='white', width=38)
website_input.grid(columnspan=2, column=1, row=1)

email_username_input = tk.Entry(bg='white', width=38)
email_username_input.grid(columnspan=2, column=1, row=2)

password_input = tk.Entry(bg='white', width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = tk.Button(text='Generate Password', width=13)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text='Add', width=36)
add_button.grid(columnspan=2, column=1, row=5)


window.mainloop()
