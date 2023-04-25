import os
from dotenv import load_dotenv
from discord_app.services.messageconsumer import MessageConsumer
from discord_app.clients.budgetbotapiclient import BudgetBotAPIClient
from discord_app.clients.discordclient import DiscordClient

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')

budget_bot_api_client = BudgetBotAPIClient(API_KEY)
message_consumer = MessageConsumer(budget_bot_api_client)
discord_client = DiscordClient(message_consumer)