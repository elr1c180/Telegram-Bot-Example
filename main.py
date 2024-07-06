import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, callback_handler, text

# Запуск бота
async def main():
    bot = Bot(token="")
    dp = Dispatcher()
    # инициализация роутеров для того, чтобы получать сообщения
    dp.include_routers(
        start.start_router,
        callback_handler.callback_router,
        text.text_router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())