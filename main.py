import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import handler_router
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(bot=bot)

async def main_telegram():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    dp.include_router(handler_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main_telegram())