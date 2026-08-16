from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

#Widget
input = Entry(width=10)
input.grid(column=1, row=0)

mile_unit = Label(text="Miles")
mile_unit.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)

def button_clicked():
    text_filled = float(input.get())
    text_filled *= 1.609
    result.config(text=f"{text_filled}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()