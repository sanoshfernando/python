import smtplib

import requests
from datetime import datetime

from streamlit import connection
MY_GMAIL = "sanoshdemian@gmail.com"
MY_PASSWORD = "ipqnfqyzyhebcsco"
MY_LAT = 55.005400 # Your latitude
MY_LONG = -1.605266 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now>=sunset or time_now<=sunrise:
        return True
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_GMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_GMAIL,
        to_addrs=MY_GMAIL,
        msg="Subject:Look Up\n\nISS in the sky above"
    )
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



