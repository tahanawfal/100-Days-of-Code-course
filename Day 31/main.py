from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

canvas = Canvas(height=526, width=800)
logo_img = PhotoImage(file="./Day 31/images/card_front.png")
canvas.create_image(300, 400, image=logo_img)
canvas.grid(row=0, column=0)

# Info
french_word = canvas.create_text(400, 150, text="french", fill="black", font=(FONT_NAME, 40, "italic"))
english_word = canvas.create_text(400, 263, text="english", fill="black", font=(FONT_NAME, 60, "bold"))



# Buttons
right_image = PhotoImage(file="./Day 31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1,row=1)

wrong_image = PhotoImage(file="./Day 31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0,row=1)

window.mainloop()