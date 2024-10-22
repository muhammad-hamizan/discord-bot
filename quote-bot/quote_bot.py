import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

# Creates a new Discord client instance
client = discord.Client()

# List of words/phrases that the bot will look for in messages to detect sadness
sad_words = ["I'm sad", "I'm depressed", "I'm unhappy", "I'm miserable"]

# Default list of encouraging messages that can be sent when a sad word is detected
starter_encouragements = [
  "You can do it",
  "You are a great person"
]

# Initializes the "responding" state in the database, enabling/disabling bot responses
if "responding" not in db.keys():
  db["responding"] = True

# Function to get a random inspirational quote from an API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

# Function to add a new encouraging message to the database
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

# Function to delete an encouraging message from the database by index
def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

# Event handler that runs when the bot is ready and logged in
@client.event
async def on_ready():
  # Prints a message to the console indicating the bot is online
  print('We have logged in as {0.user}'.format(client))

# Event handler that processes each message sent in a channel
@client.event
async def on_message(message):
  # If the message is sent by the bot itself, do nothing
  if message.author == client.user:
    return

  # Content of the message
  msg = message.content

  # If the message starts with '#inspire', the bot sends an inspirational quote
  if msg.startswith('#inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  # Check if the bot is currently set to respond to sad words
  if db["responding"]:
    # Combine starter_encouragements with any custom encouragements from the database
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    # If any sad word is found in the message, the bot sends a random encouraging message
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  # If the message starts with '#new', add a new encouraging message to the database
  if msg.startswith("#new"):
    encouraging_message = msg.split("#new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  # If the message starts with '#del', delete an encouraging message by its index
  if msg.startswith("#del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("#del", 1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  # If the message starts with '#list', display all stored encouraging messages
  if msg.startswith("#list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  # If the message starts with '#responding', toggle the bot's responding state
  if msg.startswith("#responding"):
    value = msg.split("#responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

# Keeps the bot alive by running the web server
keep_alive()

# Starts the bot using the token stored in the environment variable "TOKEN"
client.run(os.getenv('TOKEN'))
