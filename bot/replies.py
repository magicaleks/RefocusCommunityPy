import discord

_colors = {
    'green': discord.Color.from_rgb(90, 224, 110),
    'red':  discord.Color.from_rgb(224, 90, 90),
    'blue':  discord.Color.from_rgb(90, 128, 224),
    'neutral': discord.Color.from_rgb(47,49,54),
}

REPLIES = {
    'verify message': 'Hit the green button under the message to pass verification'
}

EMBEDS = {
    'already verified': discord.Embed(description="You're already verified", color=_colors['blue']),
    'verify message': discord.Embed(title="Verification", description="Hit the green button under the message to pass verification", color=_colors['blue']),
    'support message': discord.Embed(title="Contacting support", description="Our supports will contact you soon", color=_colors['blue']),
    'help message': {
        'general': discord.Embed(title="Help", description="Here help message", color=_colors['blue']),
        'unknown command': discord.Embed(title="Help", description="Unknown command provided", color=_colors['red']),
    }
}

def welcome_message(member: discord.Member):
    return discord.Embed(title="Welcome", description=f"Hi, **{member.name}**, we're glad to see you on **{member.guild.name}**", color=_colors['blue']),

def support_message(message: discord.Message):
    embed = discord.Embed(title=f"Message from {message.author.display_name}#{message.author.discriminator}", description=message.content, color=_colors['blue'])
    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar)
    embed.timestamp = message.created_at
    return embed

def verification_result(email, name, phone, fb, mention):
    embed = discord.Embed(title="Verification request",
                          description=f"**Email:** {email}\n**Name:** {name}\n**Phone:** {phone}\n**Facebook:** {fb}\n**Mention:** {mention}", color=_colors['blue'])
    return embed
