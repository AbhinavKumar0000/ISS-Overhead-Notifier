from datetime import datetime
import requests
from twilio.rest import Client

endpoint = "https://pro.openweathermap.org/data/2.5/forecast"
api_key = "1b623690d1841bd2d55b902d99eabfbf"
account_sid = "" #Twilio account SID 
auth_token = "" #Twilio authentication key

MY_LAT =  # Your latitude For testing purpose
MY_LONG =  # Your longitude



def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if  MY_LAT - 10 <= iss_latitude <= MY_LAT + 10 and MY_LONG- 10 <= iss_longitude <= MY_LONG+ 10:
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

    time_now = datetime.now().hour

    if time_now >= sunset  or time_now<= sunrise:
        return  True

if is_iss_overhead() and is_night():

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Subject:Look UP👆\n\nThe ISS 🛰🌙 is above you in the sky.",
        from_="+18596970391",
        to="+918383951265",
    )
    print(message.status)




