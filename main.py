import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot("7064652779:AAFYhpVWW-4Q0XAbrlggGCRjvdJqxy_lInA")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message(Command("cube"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("ball"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🏀")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




