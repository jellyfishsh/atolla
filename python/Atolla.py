import discord
import botData as bot

class Atolla(discord.Client):

    #Events
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    #Commands

    


client = Atolla(intents=bot.getIntents())

bot.runClient(client)
