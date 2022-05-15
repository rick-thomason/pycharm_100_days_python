import tkinter as tk


# create function to change label text to what is typed in the entry field when button is clicked
def button_clicked():
    new_input = user_input.get()
    label.config(text=new_input)


window = tk.Tk()
window.title('MY First GUI Program')
window.minsize(width=500, height=300)

# Create a Label
label = tk.Label(text='My First Label', fg='black', font=('Fira Code', 20))
label.grid(column=0, row=0)

# Create a Button
button = tk.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

new_button = tk.Button(text='New Button', command=button_clicked)
new_button.grid(column=2, row=0)

# Create Entry Component
user_input = tk.Entry(bg='white', fg='black', width=10)
user_input.grid(column=3, row=2)

window.mainloop()
