import discord
import botData as data


bot = data.getCommandBot()
guild = data.getPersonalGuild()

#Slash command
@bot.tree.command(name="hello",description="The essential command", guild=guild)
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command(name="count", description="Another interesting command", guild=guild)
async def count(interaction:discord.Interaction, arg: int):
    next = arg + 1
    await interaction.response.send_message(f"Look, I can count as well! The next number is {next}")


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