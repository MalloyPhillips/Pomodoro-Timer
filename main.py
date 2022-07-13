from tkinter import *

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Program")
window.config(pady=50, padx=90, bg=YELLOW)

# Set up canvas, add tomato img, add timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Timer label create & place
timer_label = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

# Create 'Start' and 'Reset' buttons
start_button = Button(text="Start")
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=3, column=2)

# Add check mark label
check_label = Label(bg=YELLOW, fg=GREEN, text="✓", font=(FONT_NAME, 16, "bold"))
check_label.grid(row=4, column=1)

window.mainloop()
