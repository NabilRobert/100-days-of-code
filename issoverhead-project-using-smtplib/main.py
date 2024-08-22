import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "SENDER EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"
TO_EMAIL = "YOUR EMAIL HERE"
MY_LAT = "YOUR LATITUDE" # Your latitude
MY_LONG = "YOUR LONGITUDE"  # Your longitude

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()


# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # response.raise_for_status()
    # data = response.json()

    iss_lat = float(data["iss_position"]["latitute"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
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
    if time_now >= sunset or time_now <= sunrise:
        return True

# runs code for 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(f"{MY_EMAIL}", f"{MY_PASSWORD}")
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look Up! \n\n The ISS is above the sky, the government's taking a piss!"
        )
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

