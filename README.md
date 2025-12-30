# Luckie Bot
Personal repository for my Discord Bot Luckie.

## 🤖 Commands
- `/guilds` — Lists all servers the bot is in (owner-only)
- `/server` — Shows server information
- `/user [user]` — Displays user info; defaults to yourself
- `/perms [user]` — Shows a user’s permissions in the current channel
- `/avatar [user]` — Shows a user’s avatar
- `/echo` channel message — Sends a message in a specified channel (Requires `Manage Messages` permission)
- `/purge limit [channel] [user] [word]` — Deletes messages (Requires `Manage Messages` permission)
    - `limit` — number of messages to delete (1–100)
    - `channel` — optional, defaults to current
    - `user` — optional, filter by user
    - `word` — optional, filter by keyword

## 🛠️ Built With
- `Python 3.13`
- `discord.py 2.6.4`