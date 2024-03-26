# @dp.message(Command("location"))
# async def get_locations(message: types.Message):
#     await message.answer_location(41.3239474, 69.241994)
#
#
# @dp.message(Command("contacts"))
# async def get_contacts(message: types.Message):
#     await message.answer_contacts("", message.from_user.full_name)
#
#
# @dp.callback_query(F.data == 'contacts')
# async def contacts(callback: types.CallbackQuery):
#     await callback.message.answer_contact(,", "Alixon", "Imamov")
#
#
# @dp.callback_query(F.data == "location")
# async def location(callback: types.CallbackQuery):
#     await callback.message.answer_location(41.3239474, 69.241994)
#
#
# @dp.callback_query(F.data == "card")
# async def card(callback: types.CallbackQuery):
#     await callback.message.answer("2505 0144 0635 0147")
#
#
# @dp.callback_query(F.data == "Menu")
# async def Menu(message: types.Message):
#     await message.answer_photo(photo=FSInputFile('images (7).jpg'))
