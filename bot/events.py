import logging
from discord.ext.commands import Bot, Context
from .replies import *
from .views import *
import discord

async def on_ready_event(bot: Bot):
    print(f'Bot has been started as {bot.user.name}#{bot.user.discriminator}')

async def on_message_event(bot: Bot, message: discord.Message):
    if isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
        # await bot.process_support(message)
        pass
    elif isinstance(message.channel, discord.Thread) and message.author != bot.user:
        # await bot.process_support_feedback(message)
        pass
    else:
        await bot.process_commands(message)

async def on_command_error_event(bot: Bot, ctx: Context, exc: Exception):
    logging.fatal(f'Unable to process command: {ctx.command}')

async def on_member_join_event(bot: Bot, member: discord.Member):
    await member.add_roles(ROLES.get('newbie'))
    try:
        await member.send(embed=welcome_message(member))
    except:
        pass
