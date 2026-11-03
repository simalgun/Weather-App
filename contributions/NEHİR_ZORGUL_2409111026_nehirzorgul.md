Individual Contribution
Responsible module: notifier.py

I was responsible for the notification component of our Weather App. The send_notification(topic, message) function sends rain
alerts to a specified ntfy topic using an HTTP POST request.

The module includes a notification title, UTF-8 message encoding, and a request timeout. It checks for HTTP errors and handles
request failures by printing an error message. It returns True when the request succeeds and False when a request error occurs,
allowing the calling code to check the notification result.
