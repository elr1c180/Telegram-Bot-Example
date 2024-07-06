from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards import start_kb
from pay import pay
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Подключение и инициализация API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("./c.json", scope)
client = gspread.authorize(creds)
print(client)
SHEET_ID = '1EgaH9U9cHq0iGdjSERbEE7eKUyGZhqgwcdHG0bTJtXg'
SHEET_NAME = 'list'

# Создаём роутеры для обработки callback-ответов от главного меню
callback_router = Router()
# Обратонка "Кнопки 1", срабатывает только если нажали на нее
@callback_router.callback_query(F.data == 'one')
async def one(callback: types.CallbackQuery):
    await callback.message.answer(
        'Мы находися по <a href="https://yandex.ru/maps/-/CDGynLPu">этооооому</a> адресу', 
        parse_mode='html')
    
    await callback.message.answer(
        'Выберите следующее действие:',
        reply_markup=start_kb.menu.as_markup()
    )
# Обратонка "Кнопки 2", срабатывает только если нажали на нее
@callback_router.callback_query(F.data == 'two')
async def two(callback: types.CallbackQuery):
    await callback.message.answer(
        f'Ваша персональная <a href="{pay.payment_link()}">ссылка</a> на оплату', 
        parse_mode='html')
    
    await callback.message.answer(
        'Выберите следующее действие:',
        reply_markup=start_kb.menu.as_markup()
    )
# Обратонка "Кнопки 3", срабатывает только если нажали на нее
@callback_router.callback_query(F.data == 'three')
async def three(callback: types.CallbackQuery):
    photo = FSInputFile('./img/1.jpeg')
    await callback.message.answer_photo(photo, caption='Тестовое описание')
    
    await callback.message.answer(
        'Выберите следующее действие:',
        reply_markup=start_kb.menu.as_markup()
    )
# Обратонка "Кнопки 4", срабатывает только если нажали на нее
@callback_router.callback_query(F.data == 'four')
async def three(callback: types.CallbackQuery):
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    print(sheet)
    cell_value = sheet.acell('A2').value

    await callback.message.answer(f'{cell_value}')

    await callback.message.answer(
        'Выберите следующее действие:',
        reply_markup=start_kb.menu.as_markup()
    )