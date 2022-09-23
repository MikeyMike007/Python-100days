# Program will send you a SMS reminder and ask you to bring a umbrella if its raining today

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = os.environ.get("SECRET_API_KEY")
account_sid = os.environ.get("SECRET_ACCOUNT_SID")
auth_token = os.environ.get("SECRET_AUTH_TOKEN")

twilio_virtual_num = "YOUR TWILIO VIRTUAL NUMBER HERE"
twilio_verified_number = "YOUR TWILIO VERIFIED NUMBER"

lat = "YOUR_LATITUDE_POSTITION"
lon = "YOUR_LONGITUDE_POSITION"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=twilio_virtual_num,
        to=twilio_verified_number,
    )
    print(message.status)
