import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
TOKEN=os.getenv("TOKEN")

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Whe have logged in as {client.user}')

client.run(TOKEN)