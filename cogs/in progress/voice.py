import discord
from discord.errors import ClientException
from caladrius import change_status
from discord import activity
from discord.enums import Status
from discord.ext import commands

class bot_setup(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self,ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
            await ctx.send('I joined your voice channel.')
        else:
            await ctx.send('You are not connected to a voice channel.')

    @commands.command(pass_context=True)
    async def leave(self,ctx):
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send('I left the voice channel.')
        else: 
            await ctx.send('I am not in a voice channel.')

    @commands.command(pass_context=True)
    async def pause(self,ctx):
        voice = discord.utils.get(self.voice_client,guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Not playing any sounds atm.")
    
    @commands.command(pass_context=True)
    async def resume(self,ctx):
        voice = discord.utils.get(self.voice_client,guild=ctx.guild)
        if voice.is.paused():
            voice.resume()
        else: 
            await ctx.send('No sound is paused.')

    @commands.command(pass_context=True)
    async def play(self,ctx):
        voice = ctx.guild.voice_client
        


    @commands.command(pass_context=True)
    async def stop(self,ctx):
        voice = discord.utils.get(self.voice_client,guild=ctx.guild)
        voice.stop()

def setup(client):
    client.add_cog(bot_setup(client))