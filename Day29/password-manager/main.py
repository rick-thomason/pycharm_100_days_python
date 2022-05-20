import json
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)
    # print(f"Your password is: {password}")

    # using pyperclip to automatically copy generated password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website_data = website_input.get().title()
    email_data = email_username_input.get().lower()
    password_data = password_input.get()
    new_data = {
        website_data: {
            'email': email_data,
            'password': password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0 or len(email_data) == 0:
        messagebox.showwarning(title='Oooops!', message='You must fill in all fields')
    else:
        try:
            with open('data.json', 'r') as file:
                # reading the data from file
                data = json.load(file)
                # updating the data
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                # writing the updated data to file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')


# -----------------------------Find Password----------------------------#
def find_password():
    website = website_input.get().title()

    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error!!!', message='No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error!!!', message=f'No Details For {website} Found')


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
website_input = tk.Entry(bg='white', width=21, fg='black', insertbackground='black')
website_input.grid(column=1, row=1, sticky='EW')
website_input.focus()
email_username_input = tk.Entry(bg='white', width=38, fg='black', insertbackground='black')
email_username_input.grid(columnspan=2, column=1, row=2, sticky='EW')
email_username_input.insert(0, 'rickbthomason@yahoo.com')
password_input = tk.Entry(bg='white', width=21, fg='black', insertbackground='black')
password_input.grid(column=1, row=3)

# Buttons
search_button = tk.Button(text='Search', width=13, activeforeground='black', command=find_password)
search_button.grid(column=2, row=1, sticky='EW')
generate_password_button = tk.Button(text='Generate Password', width=13, activeforeground='black',
                                     command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='EW')
add_button = tk.Button(text='Add', width=36, activeforeground='black', command=save_data)
add_button.grid(columnspan=2, column=1, row=4, sticky='EW')

window.mainloop()
