
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp


@dp.message_handler(Command("sleep"))
async def bot_sleep(message: Message):
    await message.answer(f'Ну что ж, {message.from_user.full_name}, я спать!')
