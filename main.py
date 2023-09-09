import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
keyboard.add(KeyboardButton("Моя информация"))
keyboard.add(KeyboardButton("Картинка"))


class States(StatesGroup):
    waiting_for_name = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=keyboard)

"
@dp.message_handler(lambda message: message.text.lower() == 'моя информация', state=None)
async def get_my_info(message: types.Message):
    await States.waiting_for_name.set()
    await message.answer(f"first_name: {message.from_user.first_name}")
    await message.answer(f"id: {message.from_user.id}")
    await message.answer(f"username: {message.from_user.username}")

@dp.message_handler(lambda message: message.text.lower() == 'картинка', state=None)
async def send_random_picture(message: types.Message):
    images = os.listdir('images')
    random_image = random.choice(images)

    with open(f'images/{random_image}', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=keyboard)

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling())
