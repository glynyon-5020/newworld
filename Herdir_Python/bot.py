# bot.py
import os
import discord
import random
from discord.abc import GuildChannel 
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# @client.event
# async def on_ready():
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # print(
    #     # f'{client.user} has connected to Discord!'
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )
    
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

# clean up the above code to something simpler (This didn't work!)
# @client.event
# async def on_ready():
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # print(guild)
    # print (
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name} (id: {guild.id})'
    # )

# Another simpler option
# @client.event
# async def on_ready():
    # guild = discord.utils.get(client.guilds, name=GUILD)
    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name} (id: {guild.id})'
    # )

## Creating a subclass of Client and overriding its handler methods
# bot.py
# import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')

# client = CustomClient()
# client.run(TOKEN)
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        # f'{client.user} has connected to Discord!'
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'I\'m the human form of the :100: emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '++':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)