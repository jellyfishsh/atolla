import discord
import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path
from discord import app_commands
from discord.ext import commands

def getIntents():
    intents = discord.Intents.default()
    intents.message_content = True

    return intents

def getClient():
    return discord.Client(intents=getIntents())

def getTree():
    return discord.app_commands.CommandTree(getClient())

def getToken():
    dotenv_path = Path('../.env')
    load_dotenv(dotenv_path=dotenv_path)

    return os.getenv("TOKEN")
def getCommandBot():
    return commands.Bot(command_prefix=".",intents=getIntents())

def getPersonalGuild():
    return discord.Object(id=1212566775917580398)

def runClient(client):
    client.run(getToken())