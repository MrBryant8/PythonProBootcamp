import requests
from twilio.rest import Client

LAT = 49.15  # 42.698334 sofia
LON = 123.7  # 23.319941 sofia
API_KEY = "YOUR_API_KEY"
CODES_FOR_RAIN = (2, 3, 5, 6)

account_sid = 'YOUR_TWILIO_ACC_SID'
auth_token = 'YOUR_AUTH_TOKEN'

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'units': "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()["list"][:12]
print(data)

is_raining = False
for i in data:
    if i["weather"][0]['id'] // 100 in CODES_FOR_RAIN:
        is_raining = True

if is_raining:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to='RECEIVER_NUMBER',
        from_='TWILLIO_ACC_NUMBER',
        messaging_service_sid='SERVICE_SID',
        body="It's raining cats and dogs today.Bring an ☂."
    )

    print(message.status)
