from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import start_kb
# Создаём роутер для обработки команды /start и ответа на нее
start_router = Router()

@start_router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(
        f'Доброго времени суток, <b>{message.from_user.first_name}</b>!\nВыберете действие:', 
        reply_markup=start_kb.menu.as_markup(), 
        parse_mode='html')