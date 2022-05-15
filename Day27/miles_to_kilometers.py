import tkinter as tk


def miles_to_km_converter():
    miles = float(miles_input.get())
    miles_to_km = round(miles * 1.609344, 2)
    label_3.config(text=miles_to_km)


window = tk.Tk()
window.title('Miles to Km Converter')
window.config(padx=40, pady=20)

miles_input = tk.Entry(bg='white', fg='black', width=7)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text='Miles', fg='black')
miles_label.grid(column=2 , row=0)

label_2 = tk.Label(text='is equal to', fg='black')
label_2.grid(column=0, row=1)

label_3 = tk.Label(text='0', fg='black')
label_3.grid(column=1, row=1)

km_label = tk.Label(text='Km', fg='black')
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text='Calculate', command=miles_to_km_converter)
calculate_button.grid(column=1, row=2)



window.mainloop()