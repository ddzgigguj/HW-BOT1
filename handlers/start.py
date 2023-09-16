from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from  aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
import random
import os

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [IButton(text="Наш сайт", url="https://google.com"),
             IButton(text="Наш сайт", url="https://instagram.com"),
            ],
            [
                IButton(text="О нас", callback_data="about")
            ]
        ]
    )
    await message.answer("Привет, друзья", reply_markup=kb)

@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await  callback.answer()
    await callback.message.answer("О нас")

@start_router.message(Command("photo"))
async def send_random_picture(message: types.Message):
    images_folder = "images/"
    images = [f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

    if images:
        random_image = random.choice(images)
        file = types.FSInputFile(images_folder + random_image)
        await message.answer_photo(file)
    else:
        await message.answer("В папке с картинками нет подходящих файлов.")


@start_router.message(Command("myinfo"))
async def my_info(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    info_message = f"Ваш ID: {user_id}\nИмя: {first_name}\nUsername: @{username}"
    await message.answer(info_message)
