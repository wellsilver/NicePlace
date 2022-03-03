import discord
import time
import asyncio
#import mysql.connector
#import pickle
#import yourmother


print("Loading-")
#get time since epoch in seconds no decimal
preptime = int(time.time())
savea = "save.dll"

f = open("tokengobrr.txt", "r")
key = f.read()
client = discord.Client()
#client.activity("Pwease help for commands")

@client.event
async def on_ready():
    print("The bot is ready!")
    #get time it took to start
    preptime2 = int(time.time())
    preptimef = preptime2 - preptime
    print(f"Bot took {preptimef} seconds to start")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'being cool'))
    
@client.event
async def on_message(i):
    content = i.content.lower()
    if i.author.bot:
        print()
    else:
          # prefix
        if content.startswith('pwease'):
            # finally commands, but crappy implement

            if content.startswith('text', 7):
              sendasap=content[text.find("@")+1:].split()[0]
              i.channel.send(sendasap)
client.run(key)
