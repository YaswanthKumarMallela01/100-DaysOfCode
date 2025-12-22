import os
import requests
from datetime import datetime

"""https://app.100daysofpython.dev/dashboard
Got these credentials from the above website"""

API_KEY = os.getenv("NUTRITION_API_KEY")
APP_ID = os.getenv("NUTRITION_APP_ID")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

WEIGHT = 90
HEIGHT = 169
AGE = 19
GENDER = "male"

exercise_text = input("Tell me which exercises you did: ")

params = {
  "query": exercise_text,
  "weight_kg": WEIGHT,              # Optional: Weight in kg (1-500)
  "height_cm": HEIGHT,              # Optional: Height in cm (1-300)
  "age": AGE,                       # Optional: Age (1-150)
  "gender": GENDER,                 # Optional: "male" or "female"
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

"""Got these credentials from Sheety website"""
USER_NAME = os.getenv("NUTRITION_USER_NAME")
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"

sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"


today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_BEARER_AUTHENTICATION_PASSWORD')}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)
    print(sheet_response.text)

""" Example Output:
        Tell me which exercises you did: jogged for 10 min
        {
          "workout": {
            "date": "22/12/2025",
            "time": "20:04:54",
            "exercise": "Running",
            "duration": 10,
            "calories": 154,
            "id": 4
          }
        }
"""
