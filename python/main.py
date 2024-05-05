import discord
import commands as cmds
from dotenv import load_dotenv

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)


class Atolla(discord.Client):
    #Put all on_ready functions here
    async def on_ready(self):
        await bot.tree.sync()

    #Put all on_message functions here
    async def on_message(self, message):






intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

#probably prompt the user on docker install to put the ApplicationToken on first install
client.run()
