from caladrius import change_status
import discord
from discord import activity
from discord.enums import Status
from discord.ext import commands
import random

class hm(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        change_status.start()
        await self.client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game('under construction no touching'))
        print('The bird is soaring trough the sky.')
    
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'I fly high,\n at the speed of {self.client.latency /3600} km/h')

    @commands.command(aliases=['8ball','ask'])
    async def _8ball(self,ctx,*,question):
        responses = ['uhuh','nuhuh','ask Little_Korean_Rice_Cooker.',"ugh i don't want to answer this.",'you should really know this yourself.']
        await ctx.send(f'Some weeb asked me "{question}",\n and i said: {random.choice(responses)}')



def setup(client):
    client.add_cog(hm(client))