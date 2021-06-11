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
    await client.process_commands(message)

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


class meme(@commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def memes(self, ctx):
        memes = os.listdir("./desktop/temporary")

        if len(memes) == 1:
            return
    while meming:
        meme = random.choice(memes)
        meme = "./desktop/temporary" + meme
        memeList = meme.split(".")

        if os.path.getsize(meme) < 8388608 and memeList[len(memeList)- 1] != "md":
            meming = False

        else:
            print ("File is over 8mb")

        await ctx.message.channel.send(file = discord.File(meme)) # This one


client.run("token")
