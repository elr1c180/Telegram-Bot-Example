from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
 
# Создание главного меню для бота
menu = InlineKeyboardBuilder()

menu.row(
    types.InlineKeyboardButton(
        text="Кнопка 1",
        callback_data="one"
        ),
    types.InlineKeyboardButton(
        text="Кнопка 2",
        callback_data="two"
        ))

menu.row(
    types.InlineKeyboardButton(
        text="Кнопка 3",
        callback_data="three"
        ),
    types.InlineKeyboardButton(
        text="Кнопка 4",
        callback_data="four"
        )
)