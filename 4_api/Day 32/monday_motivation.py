import datetime as dt
import smtplib
from random import choice

from email_password import password

now = dt.datetime.now()
current_weekday = now.weekday()

my_mail = "da.tahanawfal@gmail.com"
target_mail = "tahanawfel@gmail.com"

if current_weekday == 1:
    with open("Day 32/quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = choice(all_quotes).strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=target_mail,
            msg=f"Subject:Monday Motivation\n\n{random_quote}".encode("utf-8")
        )
        connection.close()