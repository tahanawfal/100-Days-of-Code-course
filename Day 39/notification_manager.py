import os

import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    # 4. This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, city, airport_code, country):
        message = f"Low price alert! Only ${price} to fly from Baghdad-BGW to {city}-{airport_code} at {country}"
        BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        parameters = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.get(url=telegram_url, params=parameters)
        response.raise_for_status()