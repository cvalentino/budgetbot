from discord_app.constants import *

class MessageConsumer:

    def __init__(self, budget_bot_api_client):
        self.budget_bot_api_client = budget_bot_api_client

    def consume_message(self, content: str) -> str:
        # get message content without the $
        content = content[1:]
        try:
            response = self.budget_bot_api_client.post_message(content)
        except Exception as e:
            # TODO: return a useful message here
            pass
        response_message = response.json()['message']
        if 200 <= response.status_code < 300:
            return response_message
        else:
            return FAILED_ADD.format(response_message)
