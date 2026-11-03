# Personal Contribution

**Name:** Melda Mermerkaya  
**Student ID:** 2409011042  
**GitHub Username:** meldamermerkaya

## Contributions

I was responsible for developing the weather forecast data retrieval module of the weather monitoring application.

My contributions include:

- Implemented the `get_forecast(lat, lon, hours)` function to retrieve hourly precipitation probability forecasts from the Open-Meteo API.
- Configured the API request parameters for latitude, longitude, forecast duration, hourly precipitation probability, and automatic timezone selection.
- Used the `requests` library to send HTTP requests with a five-second timeout and check for unsuccessful responses.
- Parsed the API response from JSON into a Python dictionary.
- Added exception handling for connection/request errors and invalid JSON data.
- Implemented up to three request attempts, with a short increasing delay after each failed attempt.
- Returned `None` if all three attempts failed, allowing other parts of the application to identify unsuccessful data retrieval.

## Technical Details

The implementation uses Python functions, dictionaries, a `for` loop, `try`/`except` blocks, and the `requests`, `json`, and `time` modules.

The `get_forecast(lat, lon, hours)` function sends a request to the Open-Meteo forecast endpoint (`https://api.open-meteo.com/v1/forecast`). Its request specifies `precipitation_probability` as the hourly weather variable, uses the supplied coordinates and number of forecast hours, and sets the timezone to `auto`.

The function checks the HTTP response using `raise_for_status()` and parses the response with `json.loads(response.text)`. If a `requests.RequestException` or `ValueError` occurs, the function prints the attempt number and error, waits briefly using `time.sleep(attempt)`, and retries. It returns the forecast dictionary on success or `None` after three failed attempts.
