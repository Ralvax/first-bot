# Author: Me
# Date: May 29 2021
# Purpose: Discord bot Creation

# bot configuration

import os
import discord
from discord.ext import commands
from googlesearch import search
import random
import youtube_dl

client = commands.Bot(command_prefix="?")


# client = discord.Client()

@client.event
async def on_ready():
    print(f"The bot is now connected as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hi":
        await message.channel.send("Hi!")


@client.command()
async def google(ctx):
    search_content = ""
    text = str(ctx.message.content)
    for i in range(2, len(text)):
        search_content = search_content + text[i]

    for n in search(search_content, tld="co.in", num=1, stop=1, pause=2):
        await ctx.send(n)


@commands.command()
async def meme(ctx):
    pass


client.run("token")
