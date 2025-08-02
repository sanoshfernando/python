import requests
from twilio.rest import Client

# Twilio credentials (avoid sharing publicly)
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Weather API call
params = {
    "cnt": 4
}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params={
        "lat": 47.800499,
        "lon": 13.044410,
        "appid": "56ffb965f435437091020c845a88a7d4",
        "cnt": 4
    }
)
response.raise_for_status()
data = response.json()

# Check if it will rain
will_rain = False
for hour_data in data["list"]:
    weather_id = int(hour_data["weather"][0]["id"])
    if weather_id < 700:
        will_rain = True

# Send SMS if rain is expected
if will_rain:
    print("Bring an umbrella ☔")

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Bring an umbrella ☔",
        to='whatsapp:+447466609270'
    )

    print(message.status)
