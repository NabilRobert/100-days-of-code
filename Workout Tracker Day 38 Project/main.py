import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 87
HEIGHT_CM = 170
AGE = 22

SHEET_NAME = "My Workouts1"
APP_ID = os.environ.get("ENV_API_ID")
APP_KEY = os.environ.get("ENV_APP_KEY")
NUTRITIONIX_ENDPOINT = os.environ.get("NIX_ENDPOINT")

header = {
    "content-type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_params = {
    "query": input("What did you do today fatty?"),
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG,
    "age": AGE
}

response = requests.post(
    url=NUTRITIONIX_ENDPOINT,
    json=exercise_params,
    headers=header
)

json_response = response.json()
print(json_response)

# The "Sheety" part
now_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

SHEETY_HEADERS = {
    "Username": os.environ.get("ENV_USERNAME"),
    "Password": os.environ.get("ENV_PASSWORD"),
    "Authorization": os.environ.get("ENV_AUTHORIZATION")
}
SHEETY_ENDPOINT = os.environ.get('ENV_SHEET_ENDPOINT')

for exercises in json_response['exercises']:
    SHEETY_PARAMS = {
        "workout": {
            'date': now_date,
            'time': now_time,
            'exercise': exercises['name'].title(),
            'duration': exercises['duration_min'],
            'calories': exercises['nf_calories']
        }
    }
    sheet_response = requests.post(url=SHEETY_ENDPOINT,json=SHEETY_PARAMS,headers=SHEETY_HEADERS)
    print(sheet_response)
