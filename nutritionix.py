import requests
from secrets import NUTRITIONIX_API_KEY, NUTRITIONIX_APP_ID, NUTRITIONIX_ENDPOINT


class Nutritionix:

    def __init__(self):
        self.endpoint = NUTRITIONIX_ENDPOINT
        self.api_key = NUTRITIONIX_API_KEY
        self.app_id = NUTRITIONIX_APP_ID

    def send_query(self, weight, age, gender="male", height=167.64):
        headers = {
            "x-app-id": self.app_id,
            "x-app-key": self.api_key,
            "Content-Type": "application/json",
        }
        parameters = {
            "query": input("Please let us know what you did today..\n"),
            "gender": gender,
            "weight_kg": weight,
            "height_cm": height,
            "age": age
        }
        response = requests.post(
            url=self.endpoint,
            json=parameters,
            headers=headers
        )
        return response.text
