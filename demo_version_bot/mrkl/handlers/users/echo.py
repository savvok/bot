from aiogram import types
from aiogram.dispatcher.filters import ContentTypeFilter
from aiogram.types import Sticker
from loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f'{message.text} - это всё, о чём ты думаешь?')

@dp.message_handler(ContentTypeFilter(content_types=Sticker))
async def bot_echo2(message: types.Message):
    await message.answer(f'Классный стикер, разбуди, когда понадобится /help')
