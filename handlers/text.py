import datetime
from aiogram import Router, F
from aiogram.types import Message
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("./c.json", scope)
client = gspread.authorize(creds)
print(client)
SHEET_ID = '1EgaH9U9cHq0iGdjSERbEE7eKUyGZhqgwcdHG0bTJtXg'
SHEET_NAME = 'list'

text_router = Router()

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%y')
        return True
    except ValueError:
        return False

#Тут я принимаю любой текст, который отправил пользователь, также проверяю дату на корректность
@text_router.message(F.text)
async def any_text(message: Message):
    date_text = message.text
    if validate_date(date_text):
        try:
            sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
            # Получаем все данные из столбца B
            column_b = sheet.col_values(2)
            # Определяем следующую свободную строку
            next_row = len(column_b) + 1
            # Записываем дату в следующую свободную ячейку столбца B
            sheet.update_cell(next_row, 2, date_text)
            await message.answer("Дата верна")
        except gspread.exceptions.APIError as e:
            print(f"APIError: {e}")
            await message.answer("Произошла ошибка при записи в Google Таблицу.")
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.answer("Произошла ошибка при записи в Google Таблицу.")
    else:
        await message.answer("Дата неверна")