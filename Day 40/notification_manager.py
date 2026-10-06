import os

import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    # 4. This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        
        BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        self.telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    def formatted_message(self, price, city, airport_code, country):
        return f"Low price alert! Only ${price} to fly from Baghdad-BGW to {city}-{airport_code} at {country}"
        
    def send_message(self, message):
        self.parameters = {
            "chat_id": self.CHAT_ID,
            "text": message
        }
        response = requests.get(url=self.telegram_url, params=self.parameters)
        response.raise_for_status()