from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIMER = None

try:
    df = pd.read_csv("Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("Day 31/data/french_words.csv")
finally:
    df_dict = df.to_dict(orient="records")
random_card = {}

# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global TIMER, random_card
    random_card = choice(df_dict)
    canvas.itemconfig(bg_image, image=front_card)
    canvas.itemconfig(title_word, text="French", fill="black")
    canvas.itemconfig(lang_word, text=random_card["French"], fill="black")
    TIMER = window.after(3000, flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(bg_image, image=back_card)
    canvas.itemconfig(title_word, text="English", fill="white")
    canvas.itemconfig(lang_word, text=random_card["English"], fill="white")
    window.after_cancel(TIMER)

# ---------------------------- IS KNOWN ------------------------------- #
def is_known():
    df_dict.remove(random_card)
    next_card()
    data = pd.DataFrame(df_dict)
    data.to_csv("Day 31/data/words_to_learn.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, height=726, width=900, background=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
back_card = PhotoImage(file="./Day 31/images/card_back.png")
front_card = PhotoImage(file="./Day 31/images/card_front.png")
bg_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Info
title_word = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
lang_word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))



# Buttons
right_image = PhotoImage(file="./Day 31/images/right.png")
right_button = Button(image=right_image, command=is_known, relief='flat', highlightthickness = 0, bd = 0)
right_button.grid(column=1,row=1)

wrong_image = PhotoImage(file="./Day 31/images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, relief='flat', highlightthickness = 0, bd = 0)
wrong_button.grid(column=0,row=1)

next_card()

window.mainloop()