from discord.ext.commands import Context
from .views import *
from .replies import *
import discord

async def mverify_command(ctx: Context, channel: discord.TextChannel):
    await channel.send(embed=EMBEDS.get('verify message'), view=VerificationMessageView())

async def help_command(ctx: Context, command: str = None):
    if command:
        await ctx.send(EMBEDS.get('help message').get(command.lower(), EMBEDS.get('help message').get('unknown command')))
    else:
        await ctx.send(EMBEDS.get('help message').get('general'))
