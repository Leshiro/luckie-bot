# Luckie (Discord Bot)
![Python](https://img.shields.io/badge/Python-3.13-blue) ![discord.py](https://img.shields.io/badge/discord.py-2.6.4-blue?style=flat)

Repository for my Discord bot, Luckie. Designed for personal use and experimentation.

Luckie is a multi-feature Discord bot designed for server moderation & utility tasks.

## 🛠️ Built With
- `Python 3.13`
- `discord.py 2.6.4`

## Commands
- `/guilds` — Lists all servers it is in (owner-only)
- `/server` — Shows server information
- `/user [user]` — Displays user information
- `/perms [user]` — Shows user permissions
- `/avatar [user]` — Shows user avatar
- `/echo [channel] [message]` — Sends message in specified channel (Requires `Manage Messages` permission)
- `/purge [limit] [channel] [user] [word]` — Bulk deletes messages (Requires `Manage Messages` permission)
    - `limit` — number of messages to delete
    - `channel` — channel to delete in (optional, defaults to current channel)
    - `user` — filter by user (optional)
    - `word` — filter by keyword (optional)
