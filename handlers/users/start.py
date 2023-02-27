from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard
from loader import dp
from aiogram.utils.markdown import text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    pass
