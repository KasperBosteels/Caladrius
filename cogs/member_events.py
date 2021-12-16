import discord
from discord.ext import commands

class member_events(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} joined a server')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} was removed from a server')

def setup(client):
    client.add_cog(member_events(client))