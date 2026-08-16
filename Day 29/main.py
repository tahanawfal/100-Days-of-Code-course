from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(numbers) for _ in range(randint(2, 4))]
    numbers_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_row():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open("./Day 29/passwords.txt", "a") as pw:
            pw.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)

add_button = Button(text="Add", width=36, command=save_row)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

window.mainloop()