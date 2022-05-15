import tkinter as tk

window = tk.Tk()
window.title('MY First GUI Program')
window.minsize(width=500, height=300)

# Create a Label
my_label = tk.Label(text='My First Label', fg='black', font=('Fira Code', 20))
my_label.pack()

# Create a Button


def button_clicked():
    new_input = user_input.get()
    my_label.config(text=new_input)


my_button = tk.Button(text='Click Me', command=button_clicked)
my_button.pack()

# Create Entry Component
user_input = tk.Entry(bg='white', fg='black', width=10)
user_input.pack()


window.mainloop()