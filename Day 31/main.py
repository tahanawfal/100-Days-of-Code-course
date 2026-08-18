from random import choice
from tkinter import *
from tkinter import messagebox
import pandas as pd
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- READ DATA ------------------------------- #
df = pd.read_csv("./Day 31/data/french_words.csv")
df_dict = df.to_dict(orient="records")

# ---------------------------- Button Function ------------------------------- #
def random_word():
    random_row = choice(df_dict)
    canvas.itemconfig(title_word, text="french")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="./Day 31/images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Info
title_word = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
value_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))

# Buttons
right_image = PhotoImage(file="./Day 31/images/right.png")
right_button = Button(image=right_image, command=random_word, highlightthickness=0, borderwidth=0)
right_button.grid(column=1,row=1)

wrong_image = PhotoImage(file="./Day 31/images/wrong.png")
wrong_button = Button(image=wrong_image, command=random_word, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0,row=1)

window.mainloop()