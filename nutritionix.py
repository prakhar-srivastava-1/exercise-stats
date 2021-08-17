import requests, os
from secrets import NUTRITIONIX_ENDPOINT


class Nutritionix:

    def __init__(self):
        self.endpoint = NUTRITIONIX_ENDPOINT
        self.api_key = os.environ.get("NUTRITIONIX_API_KEY")
        self.app_id = os.environ.get("NUTRITIONIX_APP_ID")
        self.exercise_data = dict()

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
        self.exercise_data = response.json()

    def clean_data(self):
        exercise_list = self.exercise_data["exercises"]
        exercise_list_cleaned = list()
        for exercise in exercise_list:
            exercise_tasks = dict()
            exercise_tasks["duration_min"] = exercise["duration_min"]
            exercise_tasks["nf_calories"] = exercise["nf_calories"]
            exercise_tasks["name"] = exercise["name"]
            exercise_list_cleaned.append(exercise_tasks)
        return exercise_list_cleaned


