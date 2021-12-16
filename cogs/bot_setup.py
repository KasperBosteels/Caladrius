from caladrius import change_status
from discord import activity
from discord.enums import Status
from discord.ext import commands

class bot_setup(commands.Cog):

    def __init__(self,client):
        self.client = client

    

def setup(client):
    client.add_cog(bot_setup(client))