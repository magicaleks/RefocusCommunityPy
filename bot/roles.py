from discord.ext.commands import Bot
import discord

ROLES = {}

async def setup(bot: Bot):
    global ROLES
    await bot.wait_until_ready()
    guild = bot.get_guild(bot.conf.get('guild', 982958063042588702))
    ROLES['newbie'] = guild.get_role(bot.conf.get('newbie role', 982960475664949308))
    ROLES['member'] = guild.get_role(bot.conf.get('member role', 982961475578642492))
    
    ROLES['mentor digital marketing'] = guild.get_role(bot.conf.get('mentor digital marketing role', 982960741445431326))
    ROLES['student digital marketing'] = guild.get_role(bot.conf.get('student digital marketing role', 982959735781330955))
    
    ROLES['mentor data analyst'] = guild.get_role(bot.conf.get('mentor data analyst role', 982961016725979166))
    ROLES['student data analyst'] = guild.get_role(bot.conf.get('student data analyst role', 982961343529353236))
    
    ROLES['manager'] = guild.get_role(bot.conf.get('manager role', 982959406608171089))
    ROLES['manager lead'] = guild.get_role(bot.conf.get('manager lead role', 982958864523722772))
    ROLES['founder'] = guild.get_role(bot.conf.get('founder role', 982958965581312000))
    