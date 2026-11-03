"""Remember the last result so we alert only when the situation changes."""
import json
import os

STATE_FILE = "state.json"


def load_state():
    """Return True if rain was expected last time, otherwise False."""
    if not os.path.exists(STATE_FILE):
        return False
    try:
        with open(STATE_FILE) as file:
            data = json.loads(file.read())
        return data.get("rain", False) is True
    except (ValueError, AttributeError):
        return False


def save_state(is_rain):
    """Write the latest result to disk."""
    with open(STATE_FILE, "w") as file:
        file.write(json.dumps({"rain": is_rain}))


def should_notify(was_rain, is_rain):
    """Alert only on the change: no rain -> rain."""
    return is_rain and not was_rain
