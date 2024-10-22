
# Quote Bot

## Name
**Quote Bot**

## Description
Quote Bot is a Discord bot that sends inspirational quotes or uplifting messages when users express sadness in chat. The bot can detect sad phrases and respond with encouraging words from a predefined list or quotes from an external API. Users can also add or delete custom encouraging messages.

## Badges
![Python](https://img.shields.io/badge/python-3.8-blue)
![Discord](https://img.shields.io/badge/Discord.py-1.6.0-blue)

## Visuals
![Quote Bot Screenshot](https://via.placeholder.com/600x300.png?text=Quote+Bot+Screenshot)
*Example of Quote Bot responding with an encouraging quote.*

## Installation
### Prerequisites
- Python 3.8+
- [Discord Developer Account](https://discord.com/developers/applications)
- [Replit Account](https://replit.com/)

### Steps
1. **Create a Discord Bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application, then add a bot to the application.
   - Copy the bot token for later use.

2. **Set Up the Project on Replit**:
   - Create a new Repl with Python as the language.
   - Create two files: `quote_bot.py` and `keep_alive.py`.
   - Paste the bot code into `quote_bot.py` and create a web server in `keep_alive.py`.

3. **Run the Bot on Replit**:
   - Set up the bot token as a secret in Replit (`TOKEN`).
   - Run the bot to keep it alive using a service like [Uptime Robot](https://uptimerobot.com/).

## Usage
- Type `#inspire` in a Discord channel to receive a random inspirational quote.
- Add a new custom encouragement: `#new <message>`.
- Delete an encouragement: `#del <index>`.
- List all stored encouragements: `#list`.
- Turn responding to sad words on or off: `#responding true/false`.

## Support
For support, create an issue in the GitHub repository or join our Discord server for assistance.

## Roadmap
- Add more commands to provide different types of responses.
- Integrate more external APIs for varied quotes.

## Contributing
Contributions are welcome. Please follow the guidelines below:
1. Fork the project.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request when you’re ready.

## Authors and acknowledgment
Thanks to the open-source community for their inspiration and contributions to the Discord.py library.

## License
This project is licensed under the MIT License.

## Project status
The bot is actively maintained, with new features planned for the future.
