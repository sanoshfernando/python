import requests
from pprint import pprint

url = "https://api.sheety.co/2aff02192cf6e5eaa155ba4a3cf5fd54/copyOfFlightDeals/prices"

# 1. Get all rows
response = requests.get(url)
response.raise_for_status()
sheet_data = response.json()["prices"]

# 2. Loop rows and update empty iataCode
for item in sheet_data:
    if item["iataCode"] == "":
        row_id = item["id"]   # every row in Sheety has an ID
        update_url = f"{url}/{row_id}"
        body = {
            "price": {
                "iataCode": "TESTING"
            }
        }
        update_response = requests.put(update_url, json=body)
        update_response.raise_for_status()
        print(f"Updated row {row_id} → {update_response.json()}")

# 3. Re-fetch to verify changes
new_data = requests.get(url).json()["prices"]
pprint(new_data)

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.