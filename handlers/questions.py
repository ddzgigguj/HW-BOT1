from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,
ReplyKeyboardMarkup,
ReplyKeyboardRemove,
KeyboardButton
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


questions_router = Router()

class UserData(StatesGroup):
    name = State()
    age = State()
    gender = State()

@questions_router.message(F.text == 'Отмена')
@questions_router.message(Command("cancel"))
async def cancel_questions(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Опрос отменен.", reply_markup=ReplyKeyboardRemove())

@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer("Привет! Давай проведем небольшой опрос.")
    await message.answer("Как тебя зовут?")

@questions_router.message(F.text, UserData.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserData.age)
    await message.answer("Сколько тебе лет?")


@questions_router.message(F.text.isdigit, UserData.age)
async def process_age(message: Message, state: FSMContext):
    age = int(message.text)
    if age < 0 or age > 120:
        await message.answer("Пожалуйста, введите реальный возраст.")
        return
    await state.update_data(age=age)
    await state.set_state(UserData.gender)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Муж"), KeyboardButton(text="Жен")]
        ],
        resize_keyboard=True
    )
    await message.answer("Какой у тебя пол?", reply_markup=kb)


@questions_router.message(F.text, UserData.gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ['муж', 'жен']:
        kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Муж"), KeyboardButton(text="Жен")]
            ],
            resize_keyboard=True
        )
        await message.answer("Пожалуйста, выбери пол с помощью кнопок.", reply_markup=kb)
        return
    await state.update_data(gender=gender)
    data = await state.get_data()
    await message.answer(f"Спасибо за участие в опросе!\n"
                         f"Имя: {data['name']}\n"
                         f"Возраст: {data['age']}\n"
                         f"Пол: {data['gender']}",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()