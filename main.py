# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$help'):
        await message.channel.send('$help, $hello, $website, $roulette [1-6]')
    if message.content.startswith('$website'):
        await message.channel.send(embed=discord.Embed(title="BravoHome",url="https://bravohome.onrender.com"))
    if message.content.startswith('$overthrowTheGovernment'):
      await message.channel.send("Thought Crime Detected")
      file = discord.File("dictator.png", filename="dictator.png")
      embed = discord.Embed()
      embed.set_image(url="attachment://dictator.png")
      await message.channel.send(file=file, embed=embed)
      await message.channel.send('Report to a superior officer for disciplinary action')
    if message.content.startswith('$roulette'):
      if str(random.randint(1,6)) in message.content.lower():
        await message.author.send('https://discord.gg/ykCuCENmgX')
        await message.author.kick()
      else:
        await message.channel.send('Safe')

try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
