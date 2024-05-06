import discord
import discord.http
import webImages
import botData as data


bot = data.getCommandBot()
guild = discord.Object(id=1212566775917580398)

@bot.tree.command(name="duck", description="Sends a picture of a duck (or if it doesn't work, just quacks back)", guild=guild)
async def duck(interaction:discord.Interaction):
    imageurl = webImages.randomDuckImg()
    e = discord.Embed()
    e.set_image(url=imageurl)

    print("Performing command duck!")
    await interaction.response.send_message(embed=e)

@bot.tree.command(name="bunny", description="Sends a picture of a bunny or rabbit!", guild=guild)
async def bunny(interaction:discord.Interaction):
    imagedict = webImages.randomBunnyGif()
    imagemedia = imagedict["media"]
    e = discord.Embed(title="Here is a cute rabbit!")
    e.set_image(url=imagemedia["gif"])
    e.set_thumbnail(url=imagemedia["poster"])
    e.set_author(name=f"Source: {imagedict["source"]}. API by https://www.bunnies.io/")

    print("Performing command bunny!")
    await interaction.response.send_message(embed=e)

@bot.tree.command(name="ping", description="Sends the bot's latency.", guild=guild)
async def ping(interaction:discord.Interaction):

    print("Performing command ping!")
    await interaction.response.send_message(f"Pong! Latency is {bot.latency * 1000} ms")


#Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync(guild=guild)
    print(f"Works!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)


bot.run(data.getToken())