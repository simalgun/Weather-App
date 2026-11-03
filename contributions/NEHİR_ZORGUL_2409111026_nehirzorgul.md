# Personal Contribution

**Name:** Nehir Zorgul
**Student ID:** 2409111026
**GitHub Username:** nehirzorgul

## Contributions

I was responsible for the notification component of the weather monitoring application in `notifier.py`.

My contributions include:

- Implemented the `send_notification(topic, message)` function to send push notifications through ntfy using an HTTP POST request.
- Constructed the notification URL using the provided topic and configured the notification title as “Rain Alert.”
- Used UTF-8 encoding to support message text containing special characters.
- Configured a request timeout to prevent indefinite waiting during network communication.
- Added HTTP error checking with `raise_for_status()` and handled request failures using `try` and `except`.
- Returned `True` when the request succeeded and `False` when a request error occurred, allowing the calling code to check the result.

## Technical Details

The implementation uses the Python `requests` library, functions, f-strings, dictionaries, string encoding, and exception handling.

The `send_notification()` function takes a topic name and a message as parameters. It builds the ntfy URL and sends the UTF-8-encoded message using `requests.post()`, with a title header and a timeout setting.

After sending the request, `raise_for_status()` checks for HTTP errors. If a `requests.RequestException` occurs, the function prints the error details and returns `False`. Otherwise, it returns `True`. This result indicates whether the request succeeded; it does not confirm that the recipient read the notification.
