class NotificationManager:
    # 4. This class is responsible for sending notifications with the deal flight details.
    def send_telegram_message(message):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    parameters = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.get(url=telegram_url, params=parameters)
    response.raise_for_status()
    pass