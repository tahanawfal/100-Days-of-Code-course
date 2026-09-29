import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


APP_ID = os.getenv("FITNESS_APP_ID")
APP_KEY = os.getenv("FITNESS_APP_KEY")

base_url = "https://app.100daysofpython.dev"
exercise_endpoint = f"{base_url}/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

exercise_params = {
  "query": input("Tell me which exercises you did: "),
  "weight_kg": 90,
  "height_cm": 172,
  "age": 33,
  "gender": "male"
}

r = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
print(r.json)