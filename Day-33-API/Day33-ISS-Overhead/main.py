import requests, smtplib
from datetime import datetime
import time
MY_LAT = 28.6139  # Your latitude
MY_LONG = 77.2090  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def check_location():
    if (MY_LAT + 5 >= iss_latitude >= MY_LAT + 5) and (MY_LONG + 5 >= iss_longitude >= MY_LONG-5):
        if time_now_hour >= sunset or time_now_hour <= sunrise:
            send_email()

my_email = "raholverma20@gmail.com"
my_password = "fttwxryohmtkqraa"


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="rahulver345@yahoo.com",
                            msg="Subject:International space station\n\nHey, look up space station is going over your head.")

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
time_now_hour = time_now.hour
while True:
    time.sleep(60)
    check_location()
# If the ISS is close to my current position
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
