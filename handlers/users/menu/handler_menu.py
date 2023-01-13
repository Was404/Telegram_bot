from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards import menu
from aiogram.dispatcher.filters import Command, Text

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите, что-то из меню ниже", reply_markup=menu)
@dp.message_handler(Text(equals=["Меню", "Назад", "Помощь"]))
async def get_answer(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())
