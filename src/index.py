import discord
import time
import asyncio
import mysql.connector
import pickle
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

            if content.startswith('hello', 7):
              await i.reply("World")

            if content.startswith('register', 7):
              await i.reply("Registering")
              usr = i.author
              outfile = open(savea,'wb')
              pickle.dump(usr,outfile)
              await i.channel.send("Registered")

            if content.startswith('rich', 7):
              await i.reply("Imagine being rich")

            if content.startswith('epoch', 7):
              await i.reply(f"epoch is: {int(time.time())}")
              await i.channel.send(f"The epoch when server started was {preptime} so it has been online for {int(time.time()) - preptime} seconds")

            if content.startswith('bewilderment', 7):
              await i.reply("After some careful consideration, I find myself also confused")

            if content.startswith('help', 7):
              await i.reply("Help!")
              await i.channel.send("help, commands")
              await i.channel.send("rich, become rich")
              await i.channel.send("register, register for currency")

        if content.startswith('nice place is dumb'):
            await i.reply("no im not")
        if content.startswith('Im so happy'):
            await i.reply("Now I wish I had emotions")
client.run(key)
