from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard
from dataBase.base import existe_user_in_data_base, add_user_in_data_base
from loader import dp
from aiogram.utils.markdown import text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    pass
