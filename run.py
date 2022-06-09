from bot import RefocusCommunityBot
import config
import asyncio

bot = asyncio.run(RefocusCommunityBot(config.config)._run())
