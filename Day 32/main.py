import datetime as dt
import smtplib
from random import randint

import pandas as pd
from email_password import password

my_mail = "da.tahanawfal@gmail.com"
target_mail = "tahanawfel@gmail.com"

##################### Extra Hard Starting Project ######################

# 1. Upload the birthdays.csv
bdd = pd.read_csv("Day 32/birthday_wisher/birthdays.csv")
bdd_dict = {(row.month, row.day): row for (index, row) in bdd.iterrows()}


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
current_day = today.day
current_month = today.month

if (current_month, current_day) in bdd_dict:
    name = bdd_dict[(current_month, current_day)]["name"]
    email = bdd_dict[(current_month, current_day)]["email"]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_letter_number = randint(1, 3)
    with open(f"Day 32/birthday_wisher/letter_templates/letter_{random_letter_number}.txt") as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content .replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=target_mail,
            msg=f"Subject:Happy Birthday\n\n{letter_content}"
        )
        connection.close()