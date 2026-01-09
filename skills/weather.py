import requests
import os

API_KEY = os.getenv("YOUR_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city="Jamshedpur"):
    """Returns: str | None"""
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=5)
        print("Weather API status:", response.status_code)

        if response.status_code != 200:
            print("Weather API error:", response.text)
            return None

        data = response.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        return (
            f"The weather in {city_name} is {description}. "
            f"The temperature is {temp} degrees Celsius, "
            f"feels like {feels_like}."
        )

    except Exception as e:
        print("Weather exception:", e)
        return None


def get_forecast(city="Jamshedpur"):
    """Returns: str | None"""
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(FORECAST_URL, params=params, timeout=5)
        print("Forecast API status:", response.status_code)

        if response.status_code != 200:
            print("Forecast API error:", response.text)
            return None

        data = response.json()

        forecasts = data["list"][0:8:3]

        lines = []
        for item in forecasts:
            temp = item["main"]["temp"]
            desc = item["weather"][0]["description"]
            time_txt = item["dt_txt"].split(" ")[1][:5]
            lines.append(f"At {time_txt}, it will be {desc} with {temp} degrees")

        return f"Weather forecast for {city}: " + ". ".join(lines)

    except Exception as e:
        print("Forecast exception:", e)
        return None
