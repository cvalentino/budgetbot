import os
from responses import *
from dotenv import load_dotenv



class MessageConsumer:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')

    def consume_message(self, content):
        content = content.lower()
        response = None
        if content.startswith('help') or content.startswith('$help'):
            response = HELP_RESPONSE
        elif content.startswith('$'):
            response = UNKNOWN_COMMAND
        return response
