import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = "tahanawfal"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"


# ---------------- 1. Create your user account ----------------

user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=user_endpoint, json=user_params)
# print(r.text)

# ---------------- 2. Create a graph definition ----------------

graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs/"

graph_params = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "Unit": "Day",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Baghdad"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(r.text)

# ---------------- 4. Create a graph definition ----------------

post_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

post_pararms = {
    "date": today,
    "quantity": input("How many days have you finished today?: ")
}

r = requests.post(url=post_endpoint, json=post_pararms, headers=headers)
print(r.text)