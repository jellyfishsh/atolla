import discord
import botData as data


bot = data.getCommandBot()
guild = discord.Object(id=1212566775917580398)

#Slash command
@bot.tree.command(name="hello",description="The essential command", guild=guild)
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command(name="count", description="Another interesting command", guild=guild)
async def count(interaction:discord.Interaction, arg: int):
    next = arg + 1
    await interaction.response.send_message(f"Look, I can count as well! The next number is {next}")

@bot.tree.command(name="duck", description="Sends a picture of a duck (or if it doesn't work, just quacks back)", guild=guild)
async def duck(interaction:discord.Interaction):
    await interaction.response.send_message()

@bot.tree.command(name="ping", description="Sends the bot's latency.", guild=guild)
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency is {bot.latency}")


#Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync(guild=guild)
    print(f"Works!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(f'{message.author}{message.content}')


bot.run(data.getToken())