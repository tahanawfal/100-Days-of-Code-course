import os

import requests
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = os.getenv("STOCK_API")
NEWS_API = os.getenv("NEWS_API")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stocks():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API,
        "outputsize": "compact"
    }

    stock_url = "https://www.alphavantage.co/query"
    r = requests.get(stock_url, params=stock_parameters, timeout=15)

    r.raise_for_status()
    data = r.json()

    return data

def get_changes(data: dict):
    last_dates = list(data["Time Series (Daily)"])[0:2]
    price_yesterday = float(data["Time Series (Daily)"][last_dates[0]]["4. close"])
    price_day_before_yesterday = float(data["Time Series (Daily)"][last_dates[1]]["4. close"])

    price_change = (price_yesterday - price_day_before_yesterday) / price_day_before_yesterday

    if price_change > 0:
        change_perc = f"🔺 {price_change:.0%}"
    elif price_change < 0:
        change_perc = f"🔻 {abs(price_change):.0%}"
    else:
        change_perc = "No Change"
    
    return change_perc

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_articles():
    news_parameters = {
        "q": STOCK,
        "sortBy": "publishedAt",
        "apikey": NEWS_API,
        "language": "en",
        "pageSize": 3
    }

    news_url = 'https://newsapi.org/v2/everything'
    r = requests.get(news_url, params=news_parameters, timeout=15)

    r.raise_for_status()
    data = r.json()

    articles = data["articles"]

    content = ""
    for article in articles:
        content += f"""------------
        Headline: {article["title"]}
        Brief: {article["description"]}\n"""
    
    return content

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    parameters = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.get(url=telegram_url, params=parameters)

    response.raise_for_status()

stocks = get_stocks()
change_percentage = get_changes(stocks)

stock_message = f"{STOCK}: {change_percentage}\n{get_articles()}"
send_telegram_message(stock_message)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""