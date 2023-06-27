# ModMail Bot

ModMail Bot is a Discord bot designed to simplify communication between server staff and users. It provides a streamlined and organized approach to handling user queries, support requests, and feedback.

## Features

- **ModMail Conversations**: Each user is assigned a dedicated modmail channel, ensuring private and centralized communication between staff and users.
- **Effortless Reply Functionality**: Staff members can easily reply to user messages within the dedicated modmail channels. Replies are sent as direct messages to maintain privacy and enable efficient communication.
- **Role-Based Access**: Specify specific roles that have access to the reply, help, and stats commands, ensuring only authorized staff members can use the bot's features.
- **Bot Activity Stats**: Stay informed about the bot's performance and resource usage with the stats command. Monitor CPU usage, memory consumption, guild count, and member count in real-time.
- **Customization and Flexibility**: Easily customize channel names, category settings, prefixes, and more to fit your Discord server's unique requirements.

## Getting Started

To get started with ModMailBot, follow these steps:

1. Clone the repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the bot:
   - Replace `YOUR_BOT_TOKEN` in the code with your Discord bot token.
   - Replace `YOUR_GUILD_ID` with the ID of your Discord server.
   - Customize any other settings in the code as needed.
4. Run the bot: `python bot.py`

Make sure you have Python 3.7 or higher installed on your system.

## Usage

Once the bot is running and invited to your server, you can interact with it using the following commands:

- `!reply <message>`: Reply to a user's modmail message. This command can only be used by staff members with the appropriate role.
- `!help`: Display the bot's help information.
- `!stats`: Get real-time statistics about the bot's performance and resource usage.

## Contributing

Contributions to ModMailBot are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is under [MIT License](LICENSE).

## Disclaimer

ModMail Bot is a third-party application and is not affiliated with or endorsed by Discord. Use it at your own risk.

## Credits

ModMailBot was created by Penguin and is maintained by Penguin himself.
