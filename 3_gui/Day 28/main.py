from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1.5
CYCLE = 0
ACHIEVED = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global CYCLE
    CYCLE = 0
    
    window.after_cancel(TIMER)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    global CYCLE, ACHIEVED
    CYCLE += 1

    if CYCLE % 8 == 0:
        timer_sec = LONG_BREAK_MIN * 60
        title.config(text="Break", fg=RED)
        ACHIEVED += "✓"        
    elif CYCLE % 2 == 0:
        timer_sec = SHORT_BREAK_MIN * 60
        title.config(text="Break", fg=PINK)
        ACHIEVED += "✓"
    else:
        timer_sec = WORK_MIN * 60
        title.config(text="Work", fg=GREEN)
    
    checkmark.config(text=ACHIEVED)
    count_down(timer_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER
    mins = count // 60
    secs = count % 60
    canvas.itemconfig(timer_text, text=f"{mins:02d}:{secs:02d}")
    if count > 0:
       TIMER = window.after(1000, count_down, count-1)
    else:
        start_clicked()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# title
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
title.grid(column=1, row=0)

#image
# tomato_image = create_image("tomato.png")

# start button
start_button = Button(text="Start", command=start_clicked, highlightthickness=0)
start_button.grid(column=0, row=2)

# reset buttton
reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

# checkmark
checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)
window.mainloop()