import requests
import json

from constants import DEVICE_ID, AMPLITUDE_API_KEY


class AmplitudeAPI:

    @staticmethod
    def register(user_id: int):
        event_properties = {
            "user_id": user_id,
            "event_type": "Registered"
        }

        url = "https://api.amplitude.com/2/httpapi"
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

        payload = {
            "api_key": AMPLITUDE_API_KEY,
            "events": [
                {
                    "device_id": "Windows",
                    "event_type": "Registered",
                    "user_id": user_id,
                }
            ]
        }

        try:
            response = requests.post(
                url=url,
                headers=headers,
                data=json.dumps(payload)
            )

            status_code = response.status_code
            response = response.json() if status_code == 200 else response.text

            return status_code, response

        except Exception as e:
            return 500, str(e)
