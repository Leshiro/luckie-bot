# Luckie (Discord Bot)
Personal repository for my Discord bot, Luckie. Designed for personal use and experimentation.

Luckie is a multi-feature Discord bot designed for server moderation & utility tasks.

## Commands
- `/guilds` — Lists all Discord servers it is in (owner-only)
- `/server` — Shows Discord server information
- `/user [user]` — Displays Discord user information
- `/perms [user]` — Shows Discord user permissions
- `/avatar [user]` — Shows Discord user avatar
- `/echo [channel] [message]` — Sends message in specified channel (Requires `Manage Messages` Discord permission)
- `/purge [limit] [channel] [user] [word]` — Bulk deletes messages (Requires `Manage Messages` Discord permission)
    - `limit` — number of messages to delete
    - `channel` — channel to delete in (optional, defaults to current channel)
    - `user` — filter by user (optional)
    - `word` — filter by keyword (optional)

## 🛠️ Built With
- `Python 3.13`
- `discord.py 2.6.4`
