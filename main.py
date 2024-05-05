import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
bot = Bot("7064652779:AAFYhpVWW-4Q0XAbrlggGCRjvdJqxy_lInA")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


