from discord.ui import button, Button, TextInput, View, Modal, Select
from discord.enums import ButtonStyle
import discord
from .roles import ROLES
from .channels import CHANNELS
from .replies import *
from .gsheets import *


class SupportMessageView(View):
    def __init__(self,):
        super().__init__(timeout=200)

    @button(label='Answer', style=ButtonStyle(1))
    async def click_handler(self, action: discord.Interaction, button: Button):
        embed = action.message.embeds[0]
        member = action.guild.get_member_named(embed.title.split(' ')[-1])
        thread = await action.message.create_thread(name=f"{embed.author.name}'s support ticket [{member.id}]", auto_archive_duration=10080)
        await thread.add_user(action.message.author)
        await thread.add_user(action.user)
        button.disabled = True
        button.label = 'Ticket created'
        await action.message.edit(view=self)


class VerificationWindowView(Modal, title='Student verification form'):
    email = TextInput(label='email', placeholder='example@gmail.com', required=True)
    name = TextInput(label='name', placeholder='Your name', required=True)
    fb = TextInput(label='facebook', placeholder='link to your facebook', required=True)
    phone = TextInput(label='phone', placeholder='Your phone', required=True)
    '''
        product = Select(placeholder='Choose cohort. If you have enrolled after 13/06, choose "New"', min_values=0, options=[
                    discord.SelectOption(label='New', description='If you have enrolled after 13/06, choose "New"'),
                    discord.SelectOption(label='C1 Group May 6'),
                    discord.SelectOption(label='C2 Group May 13'),
                    discord.SelectOption(label='C3 Group May 20'),
                    discord.SelectOption(label='C4 Group May 27pt1'),
                    discord.SelectOption(label='C4 Group May 27pt2'),
                    discord.SelectOption(label='C5 Group June 3'),
                    discord.SelectOption(label='C6 Group June 9'),
                    discord.SelectOption(label='C7 Group June 9'),
                    discord.SelectOption(label='C8 Group June 13'),
                    discord.SelectOption(label='C9 Group June 13'),
                ])
    '''

    async def on_submit(self, action: discord.Interaction) -> None:
        await action.response.send_message('Thanks! Please wait till managers check your verify request', ephemeral=True)
        try:
            # await action.user.add_roles(ROLES.get('member'))
            '''
                some logic here ...
            '''
            # await action.user.remove_roles(ROLES.get('newbie'))
            
            await CHANNELS.get('verification backlog').send(embed=verification_result(self.email, self.name, self.phone, self.fb, action.user.mention))

        except:
            pass


class VerificationMessageView(View):
    def __init__(self):
        super().__init__(timeout=200)

    @button(label='Verify!', style=ButtonStyle(3))
    async def click_handler(self, action: discord.Interaction, button: Button):
        if ROLES.get('newbie') in action.user.roles:
            await action.response.send_modal(VerificationWindowView())
        else:
            await action.response.send_message(embed=EMBEDS.get('already verified'), ephemeral=True)

# class VerificationConfirmMessageView(View):
#    def __init__(self):
#        super().__init__(timeout=200)
#
#    @te
