# Now, we will talk about why some APIs are not free.
# Those APIs which are not available free, are one of those APIs which have the most important data within themselves.
# In order to collect the data, many efforts and lot of processes are done.
# Therefore, they can't be available free.
# But they are available for those who are in learning phase
# They are not in position to generate profit from the data that these API provides.
# But there can be people who can pretend to be above mentioned parties and try to have commercial gain.
# In order to prevent these people to achieve their goals.
# APIs providers have API keys for each customers.
# API keys are kind of personal account number and password.
# Through API keys of customers, API providers can track how much API data is used by the customers.
# In this way, they can authenticate people, authenticate their access to the priviledged data.
# And even can deny their access when the usage goes above the set limits.
# You can generate your own API key for free by signing in.
import requests
from twilio.rest import Client

MY_LONG = 81.687810
MY_LAT = 51.481130
account_sid = "AC3f9285ad579f7c084dd3691342de395f"
# AC3f9285ad579f7c084dd3691342de395f
auth_token = "39249f9f8ace934b13433b774c26d2e8"
# 39249f9f8ace934b13433b774c26d2e8
# +12546154115
parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "d15cad969a6664e8c2f376939c0e32e1",
    "exclude": "current,daily,minutely"

}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameter)
response.raise_for_status()
hourly_data = response.json()
hourly_data_weather = hourly_data["hourly"][0:12]
will_rain = False
for hours_weather in hourly_data_weather:
    if hours_weather["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    alert = "It's going to rain today. I hope, you are bringing ☔."
else:
    alert = "It's clean today. Don't bother to bring the ☔."

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=alert,
    from_='+12546154115',
    to='+918860317648'
)

print(message.status)
