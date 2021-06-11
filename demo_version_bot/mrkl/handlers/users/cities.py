from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import vuz_list, cities_list, end_magic, cities
from keyboards.default.vuz_list import vuzes
from loader import dp

@dp.message_handler(Command("vuz_list"))
async def ask_when(message: Message):
    await message.answer("Выбери город", reply_markup=cities)

@dp.message_handler(Text(equals=["Санкт-Петербург"]))
async def spb(message: Message):
    await message.answer(f"Вузы Питера",reply_markup=vuzes)

@dp.message_handler(Text(equals=["Москва (тусит)"]))
async def msk(message: Message):
    await message.answer(f"Вперёд и с песней!", reply_markup=cities)

@dp.message_handler(Text(equals=["Саратов (шутка)"]))
async def srt(message: Message):
    await message.answer(f"В один конец", reply_markup=cities)

@dp.message_handler(Text(equals=["Другой город (скоро)"]))
async def spb(message: Message):
    await message.answer(f"А есть варианты?",reply_markup=cities)

@dp.message_handler(Text(equals=["Назад"]))
async def answer_when(message: Message):
    await message.answer(f"Как скажешь, {message.from_user.first_name}. Можно пойти /sleep?",
                        reply_markup=ReplyKeyboardRemove())
