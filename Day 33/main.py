import smtplib
from datetime import datetime
from time import sleep

import requests
from email_password import password

MY_LAT = 36.206291 # Your latitude
MY_LONG = -44.008869 # Your longitude
my_mail = "da.tahanawfal@gmail.com"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    #If the ISS is close to my current position
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour()

    # and it is currently dark
    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True

# Then send me an email to tell me to look up.
while True:
    # BONUS: run the code every 60 seconds.
    sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=my_mail,
                msg=f"Subject:Look up\n\nthe ISS is above you in the sky"
            )
            connection.close()

