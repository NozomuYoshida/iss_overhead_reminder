# iss_overhead_reminder
This is a iss_overhead_reminder by Python. To use, 'smtplib' library installation required.

## Function
- Send mail automatically to the designated person whose area is being passed through by ISS.

## Setup
- Set the latitude and longitude of your living area (c.f., https://www.latlong.net/)
  - MY_LAT: your latitude (float)
  - MY_LONG: your longitude (float)
- Change the information below
  - SENDER_NAME = 'John Doe'
  - MY_EMAIL = 'example@gmail.com'
  - TO_EMAIL = 'example@gmail.com'
  - PASSWORD = 'example'
- Also you might need to change:
  - Argments of [smtplib.SMTP('smtp.gmail.com', 587)] depending on the mail server you use
  - Setting of the security level of your mail server

Comfirmed to work on:
- MacOS (11.52)
- PyCharm 2021.02 (Community Edition)
