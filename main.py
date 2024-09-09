#https://discord.com/oauth2/authorize?client_id=1233298261582811168&response_type=code&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D1233298261582811168&scope=identify

import os
import random
import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True
id = 738235079947583590

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$uptime'):
        user = message.author
        await user.send("Uptime ping")
        async def uptimePing():
            while True:
                await asyncio.sleep(300)  # 5 minutes in seconds
                await user.send("Uptime ping")
        client.loop.create_task(uptimePing())
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$help'):
        await message.channel.send('$help, $hello, $website, $roulette [1-6]')
    if message.content.startswith('$website'):
        # await message.channel.send(embed=discord.Embed(title="BravoHome",url="https://bravohome.onrender.com"))
        await message.channel.send('Website currently under development')
    if message.content.startswith('$roulette'):
        if random.randint(1, 6) == 1:
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
