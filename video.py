import discord
import discord.ext.commands import Bot
import discord.ext import commands
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "=")
@client.event
async def on_ready():
    print("Thankyou For using Frog Bot")
	await client.change_presence(game=discord.Game(name="Being Built"))
	
@client.event
async def on_message(message):
    if message.content.startswith('=help'):
	   msg = 'Sorry this command is not availible right now'.format(message)
	   await client.send_message(message.channel, msg)
	 if message.content.startswith('<@504769680150495242>'):
	   msg = 'We are working on me you will be able to use me soon!'.format(message)
	   await client.send_message(message.channel, msg)
	   
client.run(os.getenv'NTA0NzY5NjgwMTUwNDk1MjQy.DrJ6UA.R88SZCdYPO8aiUIFZms6ufBz1b8'))
