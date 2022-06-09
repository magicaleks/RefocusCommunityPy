from typing import Union
import discord

async def forward_message(channel: Union[discord.TextChannel, discord.Thread, discord.User, discord.Member], message: discord.Message):
    return await channel.send(content=message.content, stickers=message.stickers, reference=message.reference, embeds=message.embeds)
    