# Luckie

![python](https://img.shields.io/badge/python-3.13-blue) ![discord.py](https://img.shields.io/badge/discord.py-2.6.4-green)

Luckie is a Discord bot I made for moderation & utility tasks.

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

## Built With
- [Python](https://www.python.org/)
- [Discord.py](https://github.com/Rapptz/discord.py)
