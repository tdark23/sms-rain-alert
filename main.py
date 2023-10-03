import requests
from twilio.rest import Client

base_url = "https://api.open-meteo.com/v1/forecast"
account_sid = 'ACee53d051fcc3fd80530f4ad76175500f'
auth_token = '114f989877b13831de86e520694cf02d'
MY_LAT = 3.839258
MY_LONG = 11.482464

parameters = {
    "latitude": MY_LAT,
    "longitude": MY_LONG,
    "hourly": "weathercode",
    "timezone": "auto",
    "forecast_days": 1
}

try:
    response = requests.get(base_url, params=parameters)
    response.raise_for_status()
except:
    print("something went wrong")
else:
    weather_datas = response.json()
    weathercodes = weather_datas["hourly"]["weathercode"]
    sub_weathercodes = weathercodes[8:20]
    will_rain = False
    for code in sub_weathercodes:
        if code > 59:
            will_rain = True

    if will_rain:
        # sending the sms (we could have done that using emails)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Take an umbrella ☔️, it may rain today 🌧️!",
            from_='+19288008496',
            to='+237656818635'
        )
        print(message.status)
    else:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's okay, it won't rain today ⛅️ !",
            from_='+19288008496',
            to='+237656818635'
        )
        print(message.status)

