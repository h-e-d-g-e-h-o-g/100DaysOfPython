# Natural language processing is a branch of computer science or AI.
# It concerns with giving the ability to the computers to understand text or spoken words in the same way, a human can.
import requests
import os
from datetime import datetime
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = os.environ['ENV_API_KEY']
APP_ID = os.environ["ENV_APP_ID"]
today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
HOUR = today.strftime("%H:%M:%S")
header = {
   "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
YOUR_USERNAME = os.environ['ENV_YOUR_USERNAME']
YOUR_PASSWORD = os.environ['ENV_YOUR_PASSWORD']
exercise_params = {
    "query": input("What exercises, you did today?")
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
data = response.json()
exercises_list = data["exercises"]
SHEETY_API_KEY = os.environ["ENV_SHEETY_API_KEY"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts"
for exercise in exercises_list:
    sheets_params = {
        "workout": {
            "date": DATE,
            "time": HOUR,
            "exercise": (exercise["user_input"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheets_params, auth=("Arhog", "Arpit26@"))
    response_sheety.raise_for_status()
    print(response_sheety.text)




