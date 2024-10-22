
# Summon Bot

## Name
**Summon Bot**

## Description
Summon Bot is a Discord bot that allows users to tag specific individuals when certain keywords are detected in the chat. The bot can be configured to watch for a set of keywords, and when a match is found, it tags the designated person to notify them.

## Badges
![Python](https://img.shields.io/badge/python-3.8-blue)
![Discord](https://img.shields.io/badge/Discord.py-1.6.0-blue)

## Visuals
![Summon Bot Screenshot](https://via.placeholder.com/600x300.png?text=Summon+Bot+Screenshot)
*Example of Summon Bot tagging a user when a keyword is detected.*

## Installation
### Prerequisites
- Python 3.8+
- [Discord Developer Account](https://discord.com/developers/applications)
- [Replit Account](https://replit.com/)

### Steps
1. **Create a Discord Bot**:
   - Visit the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
   - Add a bot to the application and copy the bot token.

2. **Set Up the Bot on Replit**:
   - Create a new Repl with Python as the language.
   - Create two Python files: `summon_bot.py` and `keep_alive.py`.
   - Add the bot code in `summon_bot.py` and set up the keep-alive server in `keep_alive.py`.

3. **Host the Bot on Replit**:
   - Set up environment secrets in Replit for the bot token.
   - Use [Uptime Robot](https://uptimerobot.com/) to ping the Replit web server periodically and keep the bot running.

## Usage
- Add new keywords that trigger tagging: `#add_keyword <keyword>`.
- Remove a keyword: `#remove_keyword <keyword>`.
- List all the keywords: `#list_keywords`.
- Configure who to tag when a keyword is detected.

## Support
Contact us on GitHub for bug reports or feature requests. You can also join our Discord support server.

## Roadmap
- Add custom responses for each keyword.
- Allow multiple users to be tagged for the same keyword.

## Contributing
To contribute:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request once your changes are complete.

## Authors and acknowledgment
Shoutout to the contributors who help improve the bot and the maintainers of the Discord.py library.

## License
Licensed under the MIT License.

## Project status
Active development with ongoing improvements and new features planned.
