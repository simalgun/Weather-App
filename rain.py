"""Decide from the forecast whether rain is expected."""


def get_probabilities(data):
    """Return the list of rain probabilities, or None if the data is bad."""
    if not isinstance(data, dict) or "hourly" not in data:
        return None
    values = data["hourly"].get("precipitation_probability")
    if not values or None in values:
        return None
    return values


def rain_expected(data, threshold):
    """Return (is_rain, highest_probability); (None, None) if data is bad."""
    values = get_probabilities(data)
    if values is None:
        return None, None
    highest = max(values)
    return highest >= threshold, highest
