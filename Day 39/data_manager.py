import requests
import requests_cache
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache()
session = requests.Session()

class DataManager:
    # 1. This class is responsible for talking to the Google Sheet.
    def __init__(self):
      self.sheety_endpoint = "https://api.sheety.co/51a228bf37f5604377e0c44ed751e5c7/flightTracker/airports"
    
    

      r = session.get(url=self.sheety_endpoint)
  
      data = r.json()

      return data["airports"]

table = DataManager()
airports = [ ]