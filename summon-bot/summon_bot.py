import discord
import os
import random
from replit import db
from keep_alive import keep_alive

# Creates a new Discord client instance
client = discord.Client()

# Keywords for tagging user1 and the corresponding user ID
username1 = ["keyword1_to_tag_userid1", "keyword2_to_tag_userid1"]
userid1 = ["<@userid1code>"]

# Keywords for tagging user2 and the corresponding user ID
username2 = ["keyword1_to_tag_userid2", "keyword2_to_tag_userid2"]
userid2 = ["<@userid2code>"]

# Initialize the responding state in the database
# If "responding" is not already in the database, set it to True
if "responding" not in db.keys():
  db["responding"] = True

# Event handler that triggers when the bot has successfully logged in
@client.event
async def on_ready():
  # Prints a message to the console indicating the bot is online
  print('We have logged in as {0.user}'.format(client))

# Event handler that triggers whenever a new message is detected
@client.event
async def on_message(message):
  # If the message is sent by the bot itself, do nothing
  if message.author == client.user:
    return
  
  # Stores the content of the message
  msg = message.content

  # Check if the bot is currently set to respond to messages
  if db["responding"]:
    # Prepare the ID list for user1
    id1 = userid1
    # If there are any custom responses for user1's keywords in the database, add them to the list
    if "keyword1_to_tag_userid1" in db.keys():
      id1 += db["keyword1_to_tag_userid1"]

    # If any keyword for user1 is found in the message, randomly select a response and send it
    if any(word in msg for word in userid1):
      await message.channel.send(random.choice(id1))

    # Prepare the ID list for user2
    id2 = userid2
    # If there are any custom responses for user2's keywords in the database, add them to the list
    if "keyword1_to_tag_userid2" in db.keys():
      id2 += db["keyword1_to_tag_userid2"]

    # If any keyword for user2 is found in the message, randomly select a response and send it
    if any(word in msg for word in userid2):
      await message.channel.send(random.choice(id2))

# Keeps the bot alive by running the web server
keep_alive()

# Starts the bot using the token stored in the environment variable "TOKEN"
client.run(os.getenv('TOKEN'))
