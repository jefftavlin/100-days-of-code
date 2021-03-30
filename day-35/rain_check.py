import requests

key = ''
endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

weather_param = {
    "lat":55.7558,
    "lon":37.6173,
    "appid":key,
    "exclude":"current,minutely,daily"
}

response = requests.get(endpoint, params= weather_param)
response.raise_for_status()

weather_data = response.json()
data = weather_data['hourly'][:12]
check = 0

for item in data:
    if item['weather'][0]['id'] < 700:
        check += 1

if check > 0:
    print('bring an umbrella.')
