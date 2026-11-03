"""Send a push notification to the phone with ntfy."""
import requests


def send_notification(topic, message):
    """Return True if ntfy accepted the message."""
    url = f"https://ntfy.sh/{topic}"
    headers = {"Title": "Rain Alert"}
    try:
        response = requests.post(url, data=message.encode("utf-8"),
                                 headers=headers, timeout=10)
        response.raise_for_status()
        return True
    except requests.RequestException as error:
        print(f"Notification failed: {error}")
        return False
