"""Fetch the hourly rain forecast from the Open-Meteo API."""
import json
import time
import requests

URL = "https://api.open-meteo.com/v1/forecast"


def get_forecast(lat, lon, hours):
    """Return the forecast as a dict, or None if every attempt failed."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "precipitation_probability",
        "forecast_hours": hours,
        "timezone": "auto",
    }
    for attempt in range(1, 4):
        try:
            response = requests.get(URL, params=params, timeout=5)
            response.raise_for_status()
            return json.loads(response.text)
        except (requests.RequestException, ValueError) as error:
            print(f"Attempt {attempt} failed: {error}")
            time.sleep(attempt)
    return None
