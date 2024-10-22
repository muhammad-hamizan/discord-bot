import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

username1 = ["keyword1_to_tag_userid1", "keyword2_to_tag_userid1"]
userid1 = ["<@userid1code>"]

username2 = ["keyword1_to_tag_userid2", "keyword2_to_tag_userid2"]
userid2 = ["<@userid2code>"]

if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_ready():
  print('We have logged in as {0.user}', format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if db["responding"]:
    id1 = userid1
    if "keyword1_to_tag_userid1" in db.keys():
      id1 += db["keyword1_to_tag_userid1"]

    if any(word in msg for word in userid1):
      await message.channel.send (random.choice(id1))

    id2 = userid2
    if "keyword1_to_tag_userid2" in db.keys():
      id2 += db["keyword1_to_tag_userid2"]

    if any(word in msg for word in userid2):
      await message.channel.send (random.choice(id2))
    
keep_alive()
client.run(os.getenv('TOKEN'))
