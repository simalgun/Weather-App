"""Rain alert: checks the forecast and sends a notification to your phone."""
import time
from weather import get_forecast
from rain import rain_expected
from notifier import send_notification
from state import load_state, save_state, should_notify

TOPIC = "yagmur-takim7-x9k2"  # change this to your own ntfy topic
CITY = "Istanbul"
LAT, LON = 41.01, 28.98
HOURS = 3             # how many hours ahead to look
THRESHOLD = 50        # rain chance (0-100) that triggers an alert
CHECK_EVERY = 1800    # seconds between checks


def check_once():
    """Run one full check: forecast -> decision -> notification."""
    data = get_forecast(LAT, LON, HOURS)
    is_rain, highest = rain_expected(data, THRESHOLD)
    if is_rain is None:
        print("Forecast unavailable; keeping the old state.")
        return
    print(f"Rain chance in the next {HOURS}h: {highest}%")
    if should_notify(load_state(), is_rain):
        message = f"Rain expected in {CITY} ({highest}%). Take an umbrella!"
        if not send_notification(TOPIC, message):
            return
    save_state(is_rain)


def main():
    while True:
        check_once()
        time.sleep(CHECK_EVERY)


if __name__ == "__main__":
    main()
