import pprint
import requests

from datetime import datetime

API_BASE = "http://api.openweathermap.org"
API_KEY = ""


def get_weather_data(lat=None, lon=None):
    url = f"{API_BASE}/data/2.5/onecall?exclude=minutely,hourly,alerts&units=metric&lat={lat}&lon={lon}&appid={API_KEY}"
    r = requests.get(url)
    if not r.ok:
        raise requests.ConnectionError("Did not get a valid response from the server.")

    return r.json()


def get_geo(city_name, state_code="CA", country_code="US", limit=3):
    url = f"{API_BASE}/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    r = requests.get(url)
    if not r.ok:
        raise requests.ConnectionError("Did not get a valid response from the server.")

    data = r.json()
    if not data:
        raise ValueError("No matching data returned from API call.")

    matched_data = None

    # this is long-hand `for-loop` so its easier to read.
    # normally, we'd use a list comprehension instead to simplify.
    for loc in data:
        # if the city matches what we asked for _exactly_ we can stop looking and bail out.
        if loc.get("name") == city_name:
            matched_data = loc
            break

    if not matched_data:
        raise ReferenceError(f"Cannot find a matched city for '{city_name}' in response query.")

    lat = matched_data["lat"]
    lon = matched_data["lon"]

    return lat, lon


city_name = "Campbell"
lat, lon = get_geo(city_name)
data = get_weather_data(lat=lat, lon=lon)


current_weather = data.get("current")
forecast = data.get("daily")

# for fun
# print("**************************")
# for day in forecast:
#     # note this doesnt account for timezone
#     date = datetime.fromtimestamp(day.get("dt"))
#     print("------------------")
#     print(f"{date}")
#     print("------------------")
#     pprint.pprint(day)

print(f"Weather in {city_name}: Current temp = {current_weather['temp']}, humidity = {current_weather['humidity']}\n")
