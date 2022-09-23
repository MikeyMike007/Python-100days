# Following program checks whether ISS is above your sky after sunset. If yes, then the program will send you an email to
# tell you to look up

import requests
import time
from datetime import datetime
import smtplib
import os

# Insert your position on earth
MY_LAT = 51.507351
MY_LONG = -0.127758

EMAIL = "YOUR_EMAIL"
PASSWORD = os.environ.get("SECRET")
SERVER = "YOUR_SMTP_SERVER"
THRESHOLD = 5
MESSAGE = """Subject:The ISS is above you in the sky\n\n"""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (
        MY_LAT - THRESHOLD <= iss_latitude <= MY_LAT + THRESHOLD
        and MY_LONG - THRESHOLD <= iss_longitude << MY_LONG + THRESHOLD
    ):
        return True
    else:
        return False


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

    time_now = datetime.now().hour()

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


# If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.

while True:

    if is_iss_overhead() and is_night():
        with smtplib.SMTP(SERVER) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Look up\n\n{MESSAGE}",
            )
    time.sleep(60)
