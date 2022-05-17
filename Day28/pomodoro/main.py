import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    return timer_text


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = tk.Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, highlightthickness=0, bg=YELLOW, pady=10)
timer_label.grid(column=1, row=0)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(110, 130, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Buttons
start_button = tk.Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark Labels
checkmark_label = tk.Label(text='✅', fg=GREEN, bg=YELLOW, pady=10)
checkmark_label.grid(column=1, row=3)
# checkmark_label_2 = tk.Label(text='✔', fg=GREEN, bg=YELLOW)
# checkmark_label_2.place(x=85, y=230)
# checkmark_label_3 = tk.Label(text='✔', fg=GREEN, bg=YELLOW)
# checkmark_label_3.place(x=105, y=230)
# checkmark_label_4 = tk.Label(text='✔', fg=GREEN, bg=YELLOW)
# checkmark_label_4.place(x=125, y=230)


window.mainloop()
