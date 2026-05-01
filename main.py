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
OUT_OF_CONTEXT_CHANNELID = 1499200347518795877
DAILY_QUOTE_CHANNELID = 1499833472020119597

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    if not daily_quote.is_running():
        daily_quote.start()

@tasks.loop(seconds=5)
async def daily_quote():
    try:
        ooc_channel = client.get_channel(OUT_OF_CONTEXT_CHANNELID)
        quote_channel = client.get_channel(DAILY_QUOTE_CHANNELID)

        messages = []
        async for message in ooc_channel.history(limit=1000):
            if message.content.strip() != "" and "-" in message.content:
                messages.append(message.content)

        chosen_quote = random.choice(messages)
        await quote_channel.send(chosen_quote)
    
    except Exception as e:
        print(f'An error occured: {e}')
        
client.run(TOKEN)
