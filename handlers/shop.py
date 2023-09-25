from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from db.queries import get_products

shop_router = Router()

@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Манга"),
            KeyboardButton(text="Книги"),
            KeyboardButton(text="Комиксы")
        ]]
    )
    await message.answer("Выберите категорию ниже:", reply_markup=kb)

@shop_router.message(F.text == "Манга")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список манги в нашем магазине:",reply_markup=kb)
@shop_router.message(F.text == "Купить ручку")
async def show_frukt(message: types.Message):
    await message.answer(get_products()[0][1])

@shop_router.message(F.text == "Купить карандаши")
async def show_frukt(message: types.Message):
    await message.answer(get_products()[1][1])
@shop_router.message(F.text == "Купить блокнот")
async def show_frukt(message: types.Message):
    await message.answer(get_products()[2][1])

