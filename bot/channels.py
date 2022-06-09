from discord.ext.commands import Bot
import discord

CHANNELS = {}

async def setup(bot: Bot):
    global ROLES
    await bot.wait_until_ready()
    guild = bot.get_guild(bot.conf.get('guild', 982958063042588702))
    CHANNELS['verification backlog'] = guild.get_channel(bot.conf.get('verification backlog channel', 984368717590835240))
