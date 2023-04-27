from datetime import datetime
import requests
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

EXERCISE_ENDPOINTS = 'https://trackapi.nutritionix.com/v2/natural/exercise'

post_params = {
    'query': input("What exercises did u do today?"),
    "gender": "YOUR_GENDER",
    "weight_kg": "YOUR_WEIGHT",
    "height_cm": "YOUR_HEIGHT",
    "age": "YOUR_AGE",
}

response = requests.post(url=EXERCISE_ENDPOINTS, json=post_params, headers=headers)
result = response.json()['exercises'][0]

POST_SHEETY = os.environ.get("POST_SHEETY")

bearer_headers = {
    "Authorization": "Bearer {}".format(BEARER_TOKEN)
}

add_workout = {
    "workout": {
        'date': "{}".format(datetime.now().strftime("%Y-%m-%d")),
        "time": "{}".format(datetime.now().strftime("%H:%M:%S")),
        "exercise": result["name"],
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}

post_workout = requests.post(url=POST_SHEETY, json=add_workout, headers=bearer_headers)
print(post_workout.text)

# del_workout = requests.delete(url=POST_SHEETY + "/{}".format(3), headers=bearer_headers) #Row serves as ObjectID
# print(del_workout.text)
