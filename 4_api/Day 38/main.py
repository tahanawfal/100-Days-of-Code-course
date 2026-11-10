import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def fitness_query():
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

  data = r.json()
  
  return data

def sheet_input(raw_dict: dict):
  current_date = datetime.now().strftime("%Y-%m-%d")
  current_time = datetime.now().strftime("%X")

  for exercise in raw_dict["exercises"]:
    formatted_dict = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

  return formatted_dict

def sheet_post(sheet_body: dict):

  sheet_url = 'https://api.sheety.co/51a228bf37f5604377e0c44ed751e5c7/workoutTracking/workouts'

  r = requests.post(url=sheet_url, json=sheet_body)
  
  data = r.json()

  print(data["workout"])

sheet_post(sheet_input(fitness_query()))