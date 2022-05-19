import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_input.get()
    email_data = email_username_input.get()
    password_data = password_input.get()

    with open('data.txt', 'a') as file:
        file.write(f'{website_data} | {email_data} | {password_data}\n')
        website_input.delete(0, 'end')
        email_username_input.delete(0, 'end')
        password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

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
website_input = tk.Entry(bg='white', width=38, fg='black', insertbackground='black')
website_input.grid(columnspan=2, column=1, row=1, sticky='EW')
website_input.focus()

email_username_input = tk.Entry(bg='white', width=38, fg='black', insertbackground='black')
email_username_input.grid(columnspan=2, column=1, row=2, sticky='EW')
email_username_input.insert(0, 'rickbthomason@yahoo.com')

password_input = tk.Entry(bg='white', width=21, fg='black', insertbackground='black')
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = tk.Button(text='Generate Password', width=13, activeforeground='black')
generate_password_button.grid(column=2, row=3, sticky='EW')

add_button = tk.Button(text='Add', width=36, activeforeground='black', command=save_data)
add_button.grid(columnspan=2, column=1, row=4, sticky='EW')


window.mainloop()
