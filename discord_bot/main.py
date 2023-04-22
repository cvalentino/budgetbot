import os
from dotenv import load_dotenv
from messageconsumer import MessageConsumer
import discord

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

consumer = MessageConsumer()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    response = consumer.consume_message(content)

    if response:
        await message.channel.send(response)

client.run(TOKEN)

