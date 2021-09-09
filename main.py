import smtplib
import requests
from datetime import datetime
import time

SENDER_NAME = 'John Doe'
MY_EMAIL = 'example@gmail.com'
TO_EMAIL = 'example@gmail.com'
PASSWORD = 'example'
MESSAGE = 'Look up the sky! Her\'s ISS'

# https://www.latlong.net/ is useful to know the current location of your living area
# Below is in case of Tsukuba, Japan
MY_LAT = 36.177780
MY_LONG = 36.177780


def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg='subject: Look up!\n\n'
                f'{MESSAGE}'
        )


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
is_close = iss_latitude - float(5) < MY_LONG < + float(5)
# print(is_close)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

is_dark = time_now.hour > sunset or time_now.hour <= sunrise
# print(is_dark)

while True:
    time.sleep(60)
    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # run the code every 60 seconds.
    if is_close and is_dark:
        send_email()




