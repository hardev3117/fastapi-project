# weather.py
import requests

def get_temperature(city):
    response = requests.get(f"https://api.weather.com/temp?city={city}")
    if response.status_code == 200:
        data = response.json()
        return data['temperature']
    else:
        raise Exception("API call failed")


# This is the function we want to unit test
def square(num: int) -> int:
    return num * num

