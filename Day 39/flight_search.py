import os
from datetime import datetime, timedelta

import requests_cache
from dotenv import load_dotenv

load_dotenv()
session = requests_cache.CachedSession("serp_cache", expire_after=3600)

class FlightSearch:
    # 1. This class is responsible for talking to the Flight Search API.
    def __init__(self):
        departure_id = "BGW"
        FLIGHT_APP_KEY = os.getenv("SERP_API_KEY")
        tomorrow = datetime.now() + timedelta(days=1)  # noqa: DTZ005
        six_month_later = datetime.now() + timedelta(days=6 * 30)  # noqa: DTZ005
        date_range = f"{tomorrow.strftime("%Y-%m-%d")},{six_month_later.strftime("%Y-%m-%d")}"
        self.serp_endpoint = "https://serpapi.com/search?engine=google_flights_deals"
        self.search_parameters = {
            "engine": "google_flights_deals",
            "hl": "en",
            "gl": "iq",
            "type": "2",
            "currency": "USD",
            "api_key": FLIGHT_APP_KEY,
            "departure_id": departure_id,
            "outbound_date": date_range
            }
        
    def bring_deals(self):
        r = session.get(url=self.serp_endpoint, params=self.search_parameters)
        r.raise_for_status()
        self.raw_data = r.json()
        return self.raw_data