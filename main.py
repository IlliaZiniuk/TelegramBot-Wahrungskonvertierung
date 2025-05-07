import asyncio
import logging
from aiogram import Bot, Dispatcher
from secret.config import TOKEN, BOT_PROPERTIES
from commands import handlers, callbacks

bot = Bot(token=TOKEN, default=BOT_PROPERTIES)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers.router, callbacks.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
print()