import asyncio
from dotenv import load_dotenv
from os import getenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'здраствуйте {message.from_user.first_name}'
                         f' вот все команды бота /myinfo📄,\n /photo🖼')
@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await message.answer(f'идет поиск🔍')
    await message.answer(f' id✅:{message.from_user.id}')
    await message.answer(f' first_name✅:{message.from_user.first_name}')
    await message.answer(f' username✅:{message.from_user.username}')
@dp.message(Command("photo"))
async def send_photo(message: types.Message):
    file = types.FSInputFile("images/mem.jpeg")
    await message.answer_photo(file)
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())












