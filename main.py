#discord
import discord
from discord.ext import commands
from discord import app_commands

#other imports
import json
import datetime
from datetime import datetime, timezone

#bot info
with open('bot_config.json') as config_file:
    data = json.load(config_file)
TOKEN = data['token']
prefix = data['prefix']
ownerid = data['ownerid']    
game = data['game']

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

now = datetime.now(timezone.utc)

#start up 
@bot.event
async def on_ready():
    if game != "":
        await bot.change_presence(activity=discord.Game(name=game))
    await bot.tree.sync()
    message = f"""
{bot.user}
{bot.user.id}
{now.strftime(r"%H:%M:%S - %d/%m/%Y")}"""
    print(message)

#error handler
@bot.event
async def on_command_error(ctx: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, commands.CommandNotFound):
        return
    if not ctx.response.is_done():
        await ctx.response.send_message(f":warning: Error:\n```{error}```")
            
#------------Commands------------

#guilds
@bot.tree.command(name="guilds")
async def guilds(ctx: discord.Interaction):
    if ctx.user.id == ownerid:
        embed=discord.Embed(title=f"Guilds ({len(bot.guilds)})")
        for i in bot.guilds:
            value=f"ID: `{i.id}`\nOwner: {i.owner} (`{i.owner.id}`)"
            embed.add_field(name=f"{i.name}", value=value, inline=False)
        await ctx.response.send_message(embed=embed)

#user
@bot.tree.command(name="user")
async def user(ctx: discord.Interaction, user: discord.User=None): 
    if user == None:
        user = ctx.user   
    embed = discord.Embed(title=f"User: {user}", description = f"{user.mention}")
    embed.set_thumbnail(url=user.avatar)
    userinfo = f"Username: **{user}**\nUser ID: `{user.id}`\nCreated at: `{user.created_at.strftime(r"%H:%M:%S - %d/%m/%Y")}`"
    member = ctx.guild.get_member(user.id)
    if member != None:
        embed.colour = member.colour
        #customstatus
        check_customstatus = 0    
        for a in member.activities:
            if str(a.type) == "ActivityType.custom":
                if a.name != None:
                    customstatus = f"{a.emoji} {a.name}"
                else: 
                    customstatus = f"{a.emoji}"
                check_customstatus = 1
        if check_customstatus != 1:
            customstatus = "None" 
        #activities    
        activities = []
        for a in member.activities: 
            if str(a.type) != "ActivityType.custom":
                activities.append(a)
        if len(activities) > 0:
            act_string = ', '.join([str(a.name) for a in member.activities if str(a.type) != "ActivityType.custom"])
        elif len(activities) < 1:
            act_string = "None" 
        if len(member.roles) > 1:
            role_list = member.roles
            role_list.reverse()
            role_string = ' '.join([r.mention for r in role_list][:-1])
            roleinfo = f"Roles [{(len(member.roles)-1)}]: {role_string}"
        elif len(member.roles) == 1:
            roleinfo = f"Roles [0]: `None`"
        #nickname
        if member.display_name == member.name:
            nickname = "None"
        elif member.display_name != member.name:
            nickname = member.display_name
        memberinfo = f"""Joined at: `{member.joined_at.strftime(r"%H:%M:%S - %d/%m/%Y")}`
Nickname: `{nickname}`
{roleinfo}"""
        statusinfo = f"""Status: `{str(member.status).title()}`
Custom Status: `{customstatus}`
Activities: `{act_string}`"""
    else:
        memberinfo = f""":warning: User is not on server"""
        statusinfo = f""":warning: User is not on server"""
    embed.add_field(name="User Information", value=userinfo, inline=False)
    embed.add_field(name="Member Information", value=memberinfo, inline=False)
    if member != None:
        embed.add_field(name="Status Information", value=statusinfo, inline=False)    
    user_for_banner = await bot.fetch_user(user.id)
    banner = user_for_banner.banner
    if banner != None:
        embed.set_image(url=banner)    
    await ctx.response.send_message(embed=embed)

#perms
@bot.tree.command(name="perms")
async def perms(ctx: discord.Interaction, user: discord.Member=None):  
    if user == None:
        user = ctx.user
    embed = discord.Embed(title=f"{user}'s Permissions", description = user.mention, color=user.colour)
    guild_perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    channel_perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.channel.permissions_for(user) if p[1]])
    embed.add_field(name=f"Guild Permissions ({ctx.guild.name})", value=guild_perm_string, inline=False)
    if ctx.channel.category != None:
        category_perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.channel.category.permissions_for(user) if p[1]])
        embed.add_field(name=f"Category Permissions ({ctx.channel.category.name})", value=category_perm_string, inline=False)
    embed.add_field(name=f"Channel Permissions (#{ctx.channel.name})", value=channel_perm_string, inline=False)    
    await ctx.response.send_message(embed=embed)

#avatar
@bot.tree.command(name="avatar")
async def avatar(ctx: discord.Interaction, user: discord.User=None):  
    if user == None:
        user = ctx.user
    embed = discord.Embed(title=f"{user}'s Avatar", description = f"{user.mention}")
    member = ctx.guild.get_member(user.id)
    if member != None:
        embed.colour = member.colour
    url=str(user.avatar).replace(".webp",".png")
    embed.set_image(url=url)
    await ctx.response.send_message(embed=embed)

#purge
@bot.tree.command(name="purge")
@app_commands.checks.has_permissions(manage_messages=True)
async def purge(
    interaction: discord.Interaction,
    limit: int,
    channel: discord.TextChannel | None = None,
    user: discord.User | None = None,
    word: str | None = None
):
    await interaction.response.defer()
    channel = channel or interaction.channel

    def check(m: discord.Message):
        if user and m.author != user:
            return False
        if word and word.lower() not in m.content.lower():
            return False
        return True

    deleted = await channel.purge(limit=limit, check=check)

    await interaction.followup.send(f":thumbsup: Deleted **{len(deleted)}** message(s) in {channel.mention}", ephemeral=True)

#echo
@bot.tree.command(name="echo")
@commands.has_permissions(manage_messages=True)
async def echo(ctx: discord.Interaction, channel: discord.TextChannel, message: str):
    await channel.send(message)
    await ctx.response.send_message(f":thumbsup: Echoed to {channel.mention}", ephemeral=True)

#server
@bot.tree.command(name="server")
async def server(ctx: discord.Interaction):
    guild = ctx.guild
    owner = bot.get_user(ownerid)
    bots = []
    for member in guild.members:
        if member.bot == True:
            bots.append(member)
    serverinfo = f"""Server Name: **{guild.name}**
Server ID: `{guild.id}`
Created at: `{guild.created_at.strftime(r"%H:%M:%S - %d/%m/%Y")}`

Members: **{len(guild.members)}**
Users: **{len(guild.members) - len(bots)}**
Bots: **{len(bots)}**

Categories: **{len(guild.categories)}**
Channels: **{len(guild.text_channels) + len(guild.voice_channels)}**
Text Channels: **{len(guild.text_channels)}**
Voice Channels: **{len(guild.voice_channels)}**

Emojis:  **{len(guild.emojis)}**
Roles: **{len(guild.roles)-1}**

Owner: **{guild.owner}**
Owner ID: `{guild.owner.id}`"""
    embed = discord.Embed(title=guild.name, description=serverinfo)
    embed.set_thumbnail(url=guild.icon)
    await ctx.response.send_message(embed=embed)

#run
bot.run(TOKEN)