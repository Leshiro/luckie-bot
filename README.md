# Luckie

![python](https://img.shields.io/badge/python-3.13-blue)
![discord.py](https://img.shields.io/badge/discord.py-2.6.4-green)

Luckie is a Discord bot I made for moderation & utility tasks.

## List of Commands
- `/guilds` — Lists all servers it is in (owner-only)
- `/server` — Shows server information
- `/user [user]` — Displays user information
- `/perms [user]` — Shows user permissions
- `/avatar [user]` — Shows user avatar
- `/echo [channel] [message]` — Sends message in specified channel
- `/purge [limit] [channel] [user] [word]` — Bulk deletes messages
    - `limit` — number of messages to delete
    - `channel` — channel to delete in (optional, defaults to current channel)
    - `user` — filter by user (optional)
    - `word` — filter by keyword (optional)

## Setup
Clone the repository:
``` bash
git clone https://github.com/Leshiro/luckie-bot.git
``` 
Navigate into the installed folder:
``` bash
cd luckie-bot
```
Install dependencies:
``` bash
pip install -r requirements.txt
```
Create a `.json` file and name it explicitly `bot_config.json`.

Paste the following into the file and fill the information accordingly:
``` json
{
  "token": "your Discord Bot token here",
  "ownerid": your Discord ID here
}
```
Run the bot:
``` bash
python main.py
```

## Required Permissions
This bot requires the following permissions in the server:
- View Channels
- Read Message History
- Send Messages
- Embed Links
- Manage Messages

## Built With
- Python: https://www.python.org/
- Discord.py: https://github.com/Rapptz/discord.py
