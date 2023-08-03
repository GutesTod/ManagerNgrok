import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(bot=bot)

async def main_telegram():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    await register_handlers(dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main_telegram())