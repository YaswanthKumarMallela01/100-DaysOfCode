import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

OWM_endpoint = os.getenv("OWM_ENDPOINT")
API_key = os.getenv("OPEN_WEATHER_API")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 31.326015,  # -17.549859
    "lon": 75.576180,  # 145.577429
    "appid": API_key,
    "cnt": 4
}

response = requests.get(url=OWM_endpoint, params=parameters)
data = response.json()
weather_conditions = [hour_data["weather"][0]["id"] for hour_data in data["list"]]

will_rain = False
for data in weather_conditions:
    if data < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! Take an umbrella with you",
        from_=os.getenv("TWILIO_NO"),
        to=os.getenv("MY_NO"),
    )

    print(message.status)

