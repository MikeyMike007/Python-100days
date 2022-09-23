import requests
from datetime import datetime
import os

# Nutrionix API data
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "Content-Type": "application/json"}
ENDPOINT_NUTRIONIX = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "female"
WEIGHT = 100
HEIGHT = 170
AGE = 30

exercise = input("Please insert your exercise: ")


params_nutrionix = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

# Sheety API data
SHEETY_API = os.environ.get("API_KEY")
ENDPOINT_SHEETY = (
    f"https://api.sheety.co/{SHEETY_API}/myWorkouts/workouts"
)


exercises = []
response = requests.post(url=ENDPOINT_NUTRIONIX, json=params_nutrionix, headers=headers)
now = datetime.now()

for exercise in response.json()["exercises"]:
    date = now.strftime("%d/%m/%Y")
    time = f"{now.hour}:{now.second}:00"
    type = exercise["name"]
    type = type[0].upper() + type[1:]
    duration = exercise["duration_min"]
    calories = round(exercise["nf_calories"])

    params_exercise = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": type,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=ENDPOINT_SHEETY, json=params_exercise)
    print(response.text)
