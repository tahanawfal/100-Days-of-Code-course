from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I'm a label", font=("arial", 24))
my_label.pack()

def button_clicked():
    text_filled = input.get()
    my_label.config(text=text_filled)

button = Button(text="Calculate", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()