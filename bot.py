import discord
from discord.ext import commands
import psutil

intents = discord.Intents.default()
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

modmail_conversations = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await update_activity()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await bot.wait_until_ready()

        guild = bot.get_guild(YOUR_GUILD_ID)
        if guild is None:
            print("Guild not found.")
            return

        try:
            modmail_conversation = modmail_conversations.get(message.author.id)

            if modmail_conversation is None:
                forums_category = discord.utils.get(guild.categories, name="Forums Category")
                if forums_category is None:
                    forums_category = await guild.create_category("Forums Category")

                modmail_channel_name = f"modmail-{message.author.id}"
                modmail_channel = discord.utils.get(forums_category.channels, name=modmail_channel_name)

                if modmail_channel is None:
                    modmail_channel = await forums_category.create_text_channel(modmail_channel_name)

                modmail_conversation = {
                    "user": message.author,
                    "channel": modmail_channel
                }

                modmail_conversations[message.author.id] = modmail_conversation

            modmail_embed = discord.Embed(
                title="Modmail",
                description=f"New message from {message.author.mention}",
                color=discord.Color.green()
            )
            modmail_embed.add_field(name="Content", value=message.content)

            await modmail_conversation["channel"].send(embed=modmail_embed)

            await message.author.send("Your modmail message has been received by the staff. Thank you!")

        except Exception as e:
            print(f"Error: {e}")

    await bot.process_commands(message)

@bot.command()
@commands.has_role("YOUR_ROLE_NAME")
async def reply(ctx, *, content: str):
    modmail_channel = ctx.channel
    if isinstance(modmail_channel, discord.TextChannel) and modmail_channel.category and modmail_channel.category.name == "Forums Category":
        modmail_conversation = None
        for conversation in modmail_conversations.values():
            if conversation["channel"] == modmail_channel:
                modmail_conversation = conversation
                break

        if modmail_conversation is not None:
            user = modmail_conversation["user"]
            try:
                await user.send(content)
                await ctx.send("Reply sent successfully!")
            except discord.Forbidden:
                await ctx.send("Failed to send the reply.")
        else:
            await ctx.send("Invalid modmail channel. Make sure to use the `!reply` command in the correct channel.")

@bot.command()
@commands.has_role("YOUR_ROLE_NAME")
async def stats(ctx):
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    guild_count = len(bot.guilds)
    member_count = len(set(bot.get_all_members()))

    stats_embed = discord.Embed(
        title="Bot Statistics",
        color=discord.Color.blue()
    )
    stats_embed.add_field(name="CPU Usage", value=f"{cpu_usage}%")
    stats_embed.add_field(name="Memory Usage", value=f"{memory_usage}%")
    stats_embed.add_field(name="Guilds", value=guild_count)
    stats_embed.add_field(name="Members", value=member_count)

    await ctx.send(embed=stats_embed)

async def update_activity():
    activity = discord.Activity(type=discord.ActivityType.watching, name="for Modmail | !help")
    await bot.change_presence(activity=activity)

bot.run("YOUR_BOT_TOKEN")
