import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth

api_key = os.environ['KEY']
app_id = os.environ['ID']
url_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
user = os.environ['USER']
password = os.environ['PASSWORD']

query = input('Which exercises did you complete: ')

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

params = {
    "query": query,
    "gender": "male",
    "weight_kg": 84.0,
    "height_cm": 188.0,
    "age": 25
}

def get_time():
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M:%S')
    return date, time


date, time = get_time()

fitness = requests.post(url=url_endpoint, json=params, headers=headers)
google_endpoint = 'https://api.sheety.co/0bab8f6f5157e9649ab7ba88009a8ae8/myWorkouts/workouts'

exercise, duration, calories = [], [], []

for i in range(len(fitness.json()['exercises'])):
    e = fitness.json()['exercises'][i]['user_input'].title()
    d = fitness.json()['exercises'][i]['duration_min']
    c = fitness.json()['exercises'][i]['nf_calories']

    exercise.append(e)
    duration.append(d)
    calories.append(c)

for i in range(len(exercise)):
    google_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise[i],
            "duration": duration[i],
            "calories": calories[i],
        }
    }
    response = requests.post(url=google_endpoint, json=google_params, auth = (user,password))
    print(response.text)
