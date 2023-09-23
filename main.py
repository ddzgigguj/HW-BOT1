import asyncio
import logging
from bot import bot, dp
from handlers import start_router, echo_router, shop_router, questions_router
from aiogram.types import BotCommand
from db.queries import init_db, create_tables, populate_tables


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()


async def main():
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Начало"),
            BotCommand(command="info", description="Получи инфромацию о себе"),
            BotCommand(command="shop", description="Наш магазин"),
            BotCommand(command="pic", description="Получить картинку"),
        ]
    )

    dp.startup.register(on_startup)

    dp.include_router(start_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)

    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())