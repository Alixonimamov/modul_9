
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Contacts', callback_data='contacts'), InlineKeyboardButton(text="location", callback_data="location")],
    [InlineKeyboardButton(text="card", callback_data="card"), InlineKeyboardButton(text="Menu", callback_data="Menu")],
    [InlineKeyboardButton(text="delivery", callback_data="delivery"), InlineKeyboardButton(text="your contact", callback_data="your contact")]
])



# button1 = [InlineKeyboardButton(text="Button1")]
#
# inline_keyboard.inline_keyboard.append(button1)


# inline_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[[InlineKeyboardButton(text='Youtube', callback_data='youtube')],
#                      [InlineKeyboardButton(text='VK', callback_data='vk')]
#                      ]
# )