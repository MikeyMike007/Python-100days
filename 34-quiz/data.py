import requests


class QuestionData:
    def __init__(self, api_endpoint, params):
        self.api_endpoint = api_endpoint
        self.params = params
        self.fetch_data()

    def fetch_data(self):
        question_data = []
        response = requests.get(self.api_endpoint, params=self.params)
        data = response.json()
        for question in data["results"]:
            question_data.append(question)
        return question_data
