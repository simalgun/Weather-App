# Weather-App
A Python-based weather monitoring application that sends notifications when rain is expected.
# Weather Notification System 🌧️

## Project Description

Weather Notification System is a Python-based automation project that monitors weather forecasts in Istanbul and sends push notifications to a mobile phone when rain is expected.

The application uses the Open-Meteo API to retrieve hourly precipitation probabilities and determines whether rain is likely within the next few hours.

When rain is expected, the system sends a notification through ntfy. It also stores the previous weather condition to avoid sending repeated notifications when the forecast has not changed.

## Features

* Retrieves hourly precipitation forecasts using the Open-Meteo API.
* Checks the probability of rain within the next 3 hours.
* Uses a configurable probability threshold to determine whether rain is expected.
* Sends push notifications to a mobile phone using ntfy.
* Stores the previous rain status in a JSON file.
* Avoids repeated notifications by detecting changes in weather conditions.
* Retries failed API requests up to three times.
* Runs automatically at regular intervals.

## Technologies Used

* **Python:** Main programming language.
* **Requests:** Handles HTTP requests to external APIs.
* **Open-Meteo API:** Provides weather forecast data.
* **ntfy:** Delivers push notifications to mobile devices.
* **JSON:** Stores the application's previous weather state.
* **os:** Checks whether the state file exists.
* **time:** Controls the application's checking intervals.

## Project Structure

| File          | Description                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| `main.py`     | Controls the main application workflow, manages the monitoring loop, and coordinates the other modules.      |
| `weather.py`  | Connects to the Open-Meteo API and retrieves hourly precipitation probabilities.                             |
| `rain.py`     | Analyzes precipitation probabilities and determines whether rain is expected based on a specified threshold. |
| `notifier.py` | Sends push notifications to mobile devices through ntfy.                                                     |
| `state.py`    | Loads and saves the previous rain status using JSON and determines whether a new notification is necessary.  |

### Generated Files

* `state.json`: Automatically created to store the last recorded rain status and prevent repeated notifications.

## Requirements

* Python 3
* Requests library
* Internet connection
* ntfy mobile application

## Installation

Clone the repository:

```bash
git clone https://github.com/simalgun/Weather-App.git
```

Install the required library:

```bash
pip install requests
```

Install the ntfy application on your mobile phone and subscribe to the following topic:

`weather-app-000`

## Configuration

The application settings can be modified in `main.py`.

| Variable      | Default Value   | Description                                                  |
| ------------- | --------------- | ------------------------------------------------------------ |
| `CITY`        | Istanbul        | City name used in notification messages.                     |
| `LAT`, `LON`  | 41.01, 28.98    | Geographic coordinates used for weather forecasts.           |
| `HOURS`       | 3               | Number of forecast hours to check.                           |
| `THRESHOLD`   | 50              | Minimum precipitation probability required for a rain alert. |
| `CHECK_EVERY` | 1800            | Time between checks in seconds (30 minutes).                 |
| `TOPIC`       | weather-app-000 | ntfy notification topic.                                     |

## How It Works

1. `main.py` starts the monitoring process.
2. `weather.py` requests hourly precipitation data from Open-Meteo.
3. `rain.py` analyzes the forecast and finds the highest precipitation probability.
4. `state.py` checks whether rain was expected during the previous check.
5. If rain is newly expected, `notifier.py` sends a notification through ntfy.
6. `state.py` saves the latest weather status.
7. The application waits 30 minutes and repeats the process.

## Running the Application

Start the application using:

```bash
python main.py
```

The application continuously monitors the weather and checks for rain every 30 minutes.

Press `Ctrl + C` to stop the application.

## Error Handling

* Failed API requests are retried up to three times.
* Invalid or unavailable forecast data is handled without updating the previous weather state.
* Notification failures are handled without saving an unsuccessful notification as a completed alert.
* Invalid or corrupted state data is handled by returning a default state.

## Team Members

This project was developed by a team of five students.

Şimal Gün
Nehir Zorgül
Azra Taş 
İpek Öner
Melda Mermerkaya

## Contributions

Individual team member contributions are documented in the `contributions/` directory.
