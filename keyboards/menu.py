from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
        ],
        [
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Помощь")
        ],
    ],
    resize_keyboard = True
)