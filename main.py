import requests
import os
from twilio.rest import Client

api_key = os.environ.get("MY_OWN_API")
my_lon = os.environ.get("MY_LON")
my_lat = os.environ.get("MY_LAT")
one_call_api = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ.get("MY_ACCOUNT_SID")
auth_token = os.environ.get("MY_AUTH_TOKEN")

weather_params = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts",
}

res = requests.get(url=one_call_api, params=weather_params)
res.raise_for_status()
data = res.json()

hourly_data = data["hourly"][:12]
will_rain = False

for hour_data in hourly_data:
    condition_code = int(hour_data["weather"][0]["id"])

    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain, Take an Umbrella with you.",
        from_="+18506608662",
        to=os.environ.get("MY_CELLPHONE")
    )
    print(message.status)