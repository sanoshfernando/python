import requests
from datetime import datetime

# Nutritionix setup
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": "99abfec4",
    "x-app-key": "0d05b86ad26612ea8e4bad3b57fc3e96",
    "Content-Type": "application/json"
}

user_input = input("Tell me which exercises you did: ")
params = {
    "query": user_input
}

response1 = requests.post(
    url=f"{HOST_DOMAIN}{ENDPOINT}",
    headers=nutritionix_headers,
    json=params,
    auth=('sanosh','Sanosh@2006')
)
output = response1.json()

# Time setup
now = datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")

# Sheety setup
sheety_url = "https://api.sheety.co/"
USER_NAME = "2aff02192cf6e5eaa155ba4a3cf5fd54"
PROJECT_NAME = "workouts"
SHEET_NAME = "sheet1"

sheety_endpoint = f"{sheety_url}{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"

sheety_headers = {
    'Content-Type': 'application/json'
}

# Send each exercise to Sheety
for item in output["exercises"]:
    sheet_data = {
        SHEET_NAME: {
            'date': now_date,
            'time': now_time,
            'exercise': item['name'].title(),
            'duration': item['duration_min'],
            'calories': item['nf_calories']
        }
    }

    response2 = requests.post(
        url=sheety_endpoint,
        json=sheet_data,
        headers=sheety_headers,
        auth=('sanosh', 'Sanosh@2006')
    )
