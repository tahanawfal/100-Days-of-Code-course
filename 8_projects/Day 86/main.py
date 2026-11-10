from tkinter import *

sentence = "as the golden sun began to dip below the distant horizon casting long shadows across the quiet coastal town an old lighthouse keeper meticulously inspected every gear and lever of the ancient lantern ensuring that its brilliant beam would shine brightly through the gathering mist and safely guide ships away from dangerous rocky shores"



window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
canvas.create_text(100, 100, fill="darkblue", font="Times 20 italic bold", text="Click the bubbles that are multiples of two.")
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
website_entry.focus()


window.mainloop()