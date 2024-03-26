import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

dp = Dispatcher()
bot = Bot("6896813954:AAE8GKb2hSMab1c7VN3cC6QZwqWVHuk3wJo")


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"<i><b>Salom</b></i> men <i>imamovarchitects</i> botiman!", parse_mode="HTML")







async def main():
    print("Ishlayapti.....")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())