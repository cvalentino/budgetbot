import discord


class DiscordClient:

    def __init__(self, message_consumer):
        self.message_consumer = message_consumer
        self.client = self.create_client()

    def create_client(self) -> discord.Client:
        intents = discord.Intents.default()
        intents.message_content = True

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(f'Logged in as {client.user}')

        @client.event
        async def on_message(message):
            # Verify message is from another user and starts with $
            if message.author == self.client.user \
                    or not message.content.startswith('$'):
                return
            response = self.message_consumer.consume_message(message.content)
            if response:
                await message.channel.send(response)

        return client
