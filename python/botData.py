import discord
import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path


def getIntents():
    intents = discord.Intents.default()
    intents.message_content = True

    return intents

def getClient():
    return discord.Client(intents=getIntents())

def getBotToken():
    dotenv_path = Path('../.env')
    load_dotenv(dotenv_path=dotenv_path)

    return os.getenv("TOKEN")

def runClient(client):
    client.run(getBotToken())