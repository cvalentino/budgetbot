from discord_app.constants import API_BASE_URL
import requests


class BudgetBotAPIClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def post_message(self, message: str) -> requests.Response:
        url = "{}/message".format(API_BASE_URL)
        headers = {'API_KEY': self.api_key, 'content_type': 'application/json'}
        payload = {'message': message}
        response = requests.post(url, headers=headers, json=payload)
        return response
