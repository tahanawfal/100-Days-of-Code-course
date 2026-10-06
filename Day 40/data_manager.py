import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    # 3. This class is responsible for talking to the Google Sheet.
    def __init__(self):
      self.sheety_endpoint = "https://api.sheety.co/51a228bf37f5604377e0c44ed751e5c7/flightTracker/airports"
    
    def get_sheet(self, data):
      r = requests.get(url=self.sheety_endpoint,  params={"filter[arrivalAirportCode]": data["arrivalAirportCode"]})
      r.raise_for_status()
      rows = r.json()["airports"]
      return rows[0] if rows else None

    def post_sheet(self, data):
      r = requests.post(url=self.sheety_endpoint, json={"airport": data})
      r.raise_for_status()
      return r.json()["airport"]

    def put_sheet(self, data, row_id):
      r = requests.put(url=f"{self.sheety_endpoint}/{row_id}", json={"airport": data})
      r.raise_for_status()
      return r.json()["airport"]