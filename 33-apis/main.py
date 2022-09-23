import requests
from requests.api import request
from datetime import *

# Check ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()

long = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

print(f"ISS position -> long: {long} - lat: {lat}")

# Detrermine when is sunrise and when is sunset
# London
MY_LAT = 51.507351
MY_LONG = -0.127758

# You can also provide data to api endpoints
parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

# Some split parsing to determine the hour of sunrise / sunset
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(f"Sunrise hour: {sunrise}")
print(f"Sunset hour: {sunset}")
print(f"Current hour: {time_now}")
