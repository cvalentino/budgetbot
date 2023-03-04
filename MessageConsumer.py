from responses import *


class MessageConsumer:

    def __init__(self):
        self.api_key = "some key" # will be used for microservice calls in the future

    def consume_message(self, content):
        content = content.lower()
        response = None
        if content.startswith('help') or content.startswith('$help'):
            response = HELP_RESPONSE
        elif content.startswith('$'):
            response = UNKNOWN_COMMAND
        return response
