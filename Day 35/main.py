import os

import requests

# -----------------------------
# OpenWeather
# -----------------------------
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
owm_api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 14.073080,
    "lon": 98.193672,
    "appid": owm_api_key,
    "cnt": 4
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()

data = response.json()


# -----------------------------
# Check for rain
# -----------------------------
will_rain = False

for hour_data in data["list"]:
    weather_code = hour_data["weather"][0]["id"]

    if int(weather_code) < 700:
        will_rain = True
        break


# -----------------------------
# Send Telegram message
# -----------------------------
def send_telegram_message(message):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    parameters = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.get(
        url=telegram_url,
        params=parameters
    )

    response.raise_for_status()


# -----------------------------
# Alert
# -----------------------------
if will_rain:
    send_telegram_message("🌧️ Bring an umbrella!")
    print("Telegram message sent.")