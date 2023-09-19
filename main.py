import asyncio
import logging
from bot import bot, dp

from handlers import (start_router,
                      echo_router,
                      shop_router,
                      questions_router
                      )
from aiogram.types import BotCommand


async def main():
    # bot.set_my_commands(
    #     BotCommand(command="start", description="Начало"),
    #     BotCommand(command="info", description="Получи информацию о себе"),
    #     BotCommand(command="shop", description="Наш магазин"),
    #     BotCommand(command="pic", description="Получить картинку")
    # )
    dp.include_router(start_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(echo_router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


