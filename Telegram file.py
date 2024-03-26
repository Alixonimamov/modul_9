import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile


from keyboard import keyboard

dp = Dispatcher()
bot = Bot("7124627015:AAFA8X81QWfFcaL_jW_4VQcQwAItRdR8nxY")



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"<i><b>Salom</b></i> Im <i>De pari</i> Bot!", parse_mode="HTML",
                         reply_markup=keyboard)

@dp.message(Command("location"))
async def get_locations(message: types.Message):
    await message.answer_location(41.3239474, 69.241994)


@dp.message(Command("contacts"))
async def get_contacts(message: types.Message):
    await message.answer_contacts("", message.from_user.full_name)




@dp.callback_query(F.data == 'contacts')
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer_contact("+998777021602", "Alixon", "Imamov")


@dp.callback_query(F.data == "location")
async def location(callback: types.CallbackQuery):
    await callback.message.answer_location(69.280056,41.296750)


@dp.callback_query(F.data == "card")
async def card(callback: types.CallbackQuery):
    await callback.message.answer("2505 0144 0635 0147")


@dp.callback_query(F.data == "Menu")
async def Menu(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo=FSInputFile('images (7).jpg'))






async def main():
    print("Ishlayapti.....")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
