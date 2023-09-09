from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
keyboard.add(KeyboardButton("Моя информация"))
keyboard.add(KeyboardButton("Картинка"))
