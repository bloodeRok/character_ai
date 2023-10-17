import requests
import json

from constants import DEVICE_ID

headers = {
    "Content-Type": 'application/json',
    "Accept": '*/*'
}

data = {
    "api_key": AMPLITUDE_API_KEY,
    "events": [{
        "device_id": DEVICE_ID,
        "event_type": "Sign up"
    }]
}

a = json.dumps(data)

response = requests.post(
    "https://api2.amplitude.com/2/httpapi",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.text)
