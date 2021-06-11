from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Что мне не лень сделать: ',
        '/start - проснуться',
        '/help - сказать, что мне не лень сделать',
        '/vuz_list - рассказать про вузы',
        '/magic - исполнить желание',
        '/sleep - уснуть'
    ]
    await message.answer('\n'.join(text))
