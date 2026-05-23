import os
from dotenv import load_dotenv
import discord
from discord.ext import tasks
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
QUOTES_CHANNELID = int(os.getenv('QUOTES_CHANNELID'))
DAILY_QUOTE_CHANNELID = int(os.getenv('DAILY_QUOTE_CHANNELID'))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    if not daily_quote.is_running():
        daily_quote.start()


used_messages = set()

@tasks.loop(hours=24)
async def daily_quote():
    quotes_channel = client.get_channel(QUOTES_CHANNELID)
    daily_quote_channel = client.get_channel(DAILY_QUOTE_CHANNELID)

    messages = []
    async for message in quotes_channel.history(limit=1000):
        if message.content.strip() != "" and "-" in message.content:
            if message.content not in used_messages:
                messages.append(message.content)

    if not messages:
        return

    chosen_quote = random.choice(messages)
    used_messages.add(chosen_quote)
    await daily_quote_channel.send(chosen_quote)
        
client.run(TOKEN)
