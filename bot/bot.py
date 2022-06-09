from discord.ext.commands import Bot, command, Command
from .events import *
from .commands import *
from .utils import *
from . import roles
from . import channels

class RefocusCommunityBot(Bot):
    def __init__(self, config: dict):
        self.conf = config
        super().__init__(command_prefix=self.conf['prefixes'], intents=discord.Intents.all(), case_insensitive=True, strip_after_prefix=True)
    
    async def process_support(self, message: discord.Message):
        guild = self.get_guild(self.conf.get('guild'))
        member = guild.get_member(message.author.id)
        if member:
            support_channel = guild.get_channel(self.conf.get('support channel', 983593663428964392))
            for thread in support_channel.threads:
                if str(member.id) in thread.name:
                    await forward_message(thread, message)
                    return
            await support_channel.send(embed=support_message(message), view=SupportMessageView())
            
            '''
                if len(list(
                    filter(lambda m: m.author.id != self.user.id, [
                        message async for message in message.channel.history(limit=5)
                        ])) 
                    ) >= 5:
                    try:
                        await member.send(embed=EMBEDS.get('support message'))
                    except:
                        pass
            '''
    
    async def process_support_feedback(self, message: discord.Message):
        id = int(message.channel.name.split('[')[-1].split(']')[0])
        member = message.guild.get_member(id)
        await forward_message(member, message)
        '''
            if not message.content.lower().startswith(''):
                pass
        '''
    
    async def on_ready(self):
        await roles.setup(self)
        await channels.setup(self)
        await self.setup()
        await on_ready_event(self)
    
    async def on_message(self, msg: discord.Message):
        await on_message_event(self, msg)
        
    async def on_member_join(self, member: discord.Member):
        await on_member_join_event(self, member)
    
    #async def on_command_error(self, ctx, exc):
    #    await on_command_error_event(self, ctx, exc)
    
    async def setup(self):
        self.remove_command('help')
        self.add_command(Command(mverify_command, name='mverify'))
        self.add_command(Command(help_command, name='help'))
        #self.add_listener(self.on_message, 'on_message')
    
    async def _run(self):
        await self.start(self.conf['token'])
