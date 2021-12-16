import discord
from discord.ext import commands
class moderation_basics(commands.Cog):

    def __init__(self,client):
        self.client = client

    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member: discord.Member,*,reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member : discord.Member,*,reason=None):
       await member.ban(reason=reason)
       await ctx.send(f'banned user {member.mention}')

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
      banned_users = await ctx.guild.bans()
      member_name,member_discriminator = member.split('#')
      for ban_entry in banned_users:
        user = ban_entry.user
        if {user.name, user.discriminator} == {member_name, member_discriminator}:
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def eat(self,ctx,amount:int=1):
        await ctx.channel.purge(limit=amount+1)
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            await ctx.send('Command not foudn')
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('You did not give me the required argument.')        
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('I do not have the right permissions do to this.')   
    
   
        

def setup(client):
    client.add_cog(moderation_basics(client))