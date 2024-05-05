import discord

@bot.tree.command(name="helloworld", description="Atolla testing")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

