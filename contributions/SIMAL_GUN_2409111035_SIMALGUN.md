

# Personal Contribution

**Name:** Şimal Gün
**Student ID:** 2409111035
**GitHub Username:** simalgun

## Contributions

I was responsible for developing the rain prediction logic of the weather monitoring application.

My contributions include:

* Implemented the `get_probabilities()` function to retrieve precipitation probability values from hourly weather data.
* Added input validation to check whether the received data has the expected structure and contains valid precipitation information.
* Implemented the `rain_expected()` function to determine whether rain is expected based on the highest precipitation probability.
* Added error handling for invalid or incomplete weather data by returning `(None, None)` when the data cannot be processed.

## Technical Details

The implementation uses Python dictionaries, functions, conditional statements, built-in functions such as `isinstance()` and `max()`, and input validation.

The `get_probabilities()` function extracts hourly precipitation probabilities, while `rain_expected()` calculates the highest probability and compares it with a given threshold to determine whether rain is expected.
