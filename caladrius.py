import os
import discord
from discord.enums import Status
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = "+")
status = cycle(['looking for worms','with food','looking for weebs'])

@client.command()
async def load(ctx,extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx,extention):
    client.unload_extension(f'cogs.{extention}')

@client.command()
async def reload(ctx,extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(f'loading: {filename[:-3]}')
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Nzk1MDkwNjE3ODg5MzI1MDY2.X_ET1w.9UkpEYpJ-YYFFzLpwSC862yRIhk')