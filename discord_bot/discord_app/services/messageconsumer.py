from discord_app.constants import *

class MessageConsumer:

    def __init__(self, budget_bot_api_client):
        self.budget_bot_api_client = budget_bot_api_client

    def consume_message(self, content: str) -> str:
        # get message content without the $
        content = content[1:]
        response = self.budget_bot_api_client.post_message(content)
        response_message = response.json()['message']
        if response.status_code == 200:
            return response_message
        elif response.status_code == 201:
            line_item = response.json()['validation']['line_item']
            return SUCCESSFUL_ADD.format(line_item['month'], line_item['day'], \
                                           line_item['description'], line_item['cost'], line_item['category'].title())
        else:
            return FAILED_ADD.format(response_message)
