import os
from datetime import datetime, timedelta

import requests
import requests_cache
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache()
session = requests.Session()

class FlightSearch:
    # 2. This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.departure_id = "BGW"
        self.FLIGHT_APP_KEY = os.getenv("SERP_API_KEY")
        self.serp_endpoint = "https://serpapi.com/search?engine=google_flights_deals"
        self.prices_list = []
        
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_later = datetime.now() + timedelta(days=6 * 30)
        self.date_range = f"{tomorrow.strftime("%Y-%m-%d")},{six_month_later.strftime("%Y-%m-%d")}"
        self.search_parameters = {
            "engine": "google_flights_deals",
            "hl": "en",
            "gl": "iq",
            "type": "2",
            "currency": "USD",
            "api_key": self.FLIGHT_APP_KEY,
            "departure_id": self.departure_id,
            "outbound_date": self.date_range
            }

        r = session.get(url=self.serp_endpoint, params=self.search_parameters)
        r.raise_for_status()
        self.raw_data = r.json()