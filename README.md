# Discord Bot Collection

## Description
This repository contains two distinct Discord bots: **Quote Bot** and **Summon Bot**, each with its own functionality and purpose.

- **Quote Bot**: Sends inspirational quotes or uplifting messages when users express sadness in chat. The bot can detect sad phrases and respond with encouraging words or quotes from an external API.
- **Summon Bot**: Allows users to tag specific individuals when certain keywords are detected in chat. The bot can be configured to watch for a set of keywords and notify designated users.

## Badges
![Python](https://img.shields.io/badge/python-3.8-blue)
![Discord](https://img.shields.io/badge/Discord.py-1.6.0-blue)

## Installation
### Prerequisites
- Python 3.8+
- [Discord Developer Account](https://discord.com/developers/applications)
- [Replit Account](https://replit.com/)

### Steps
1. **Create a Discord Bot for Each Bot**:
   - Visit the [Discord Developer Portal](https://discord.com/developers/applications) and create two separate applications (one for each bot).
   - Add a bot to each application and copy the bot tokens.

2. **Set Up the Bots on Replit**:
   - Create a new Repl for each bot (Quote Bot and Summon Bot).
   - Add the `quote_bot.py` and `summon_bot.py` files, along with `keep_alive.py`, in the respective Repls.
   - Configure the environment variables to store bot tokens securely.

3. **Host the Bots Using Uptime Robot**:
   - Keep the Repl web servers running by using [Uptime Robot](https://uptimerobot.com/) to ping the web server periodically.

## Usage
### Quote Bot
- Trigger the bot to send an inspirational message: `#inspire`
- Manage custom messages:
  - Add a new encouragement: `#new <message>`
  - Delete an encouragement: `#del <index>`
  - List all stored encouragements: `#list`
- Control bot response to sad words: `#responding true/false`

### Summon Bot
- Add or remove keywords that trigger user tagging:
  - Add a keyword: `#add_keyword <keyword>`
  - Remove a keyword: `#remove_keyword <keyword>`
  - List all keywords: `#list_keywords`
- Configure which users to tag for each keyword.

## Support
If you encounter any issues, please open an issue in the GitHub repository or join our Discord support server for help.

## Roadmap
- **Quote Bot**:
  - Support additional APIs for quotes.
  - Allow users to submit their own quotes to the bot's database.

- **Summon Bot**:
  - Enable multiple users to be tagged for a single keyword.
  - Allow custom responses for different keywords.

## Contributing
Contributions are welcome for both bots. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Open a pull request when ready.

## Authors and acknowledgment
Special thanks to the open-source community for supporting the development of these bots.

## Project status
Both bots are actively maintained, with plans for future updates and improvements.
