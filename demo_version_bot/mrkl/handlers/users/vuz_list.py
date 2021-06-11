from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import vuz_list, cities_list, end_vuz, cities
from keyboards.default.end_vuz import endvuz
from loader import dp


@dp.message_handler(Text(equals=["Университет ИТМО"]))
async def itmo(message: Message):
    await message.answer(f"{message.text} - самый неклассический. "
                         f"Баллы появятся позже. (Но на контракт возьмут везде)",
                         reply_markup=endvuz)

@dp.message_handler(Text(equals=["СПБГУ", "ВШЭ", "Политех", "Бонч"]))
async def spb_other(message: Message):
    await message.answer(f"{message.text}? Мда", reply_markup=endvuz)

@dp.message_handler(Text(equals=["Страшно вырубай"]))
async def answer_when(message: Message):
    await message.answer(f"Уже сделано, {message.from_user.first_name}! Можно пойти /sleep?",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Пока хватит)"]))
async def smth_else2(message: Message):
    await message.answer(f"Как пожелаешь, {message.from_user.first_name}", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["В начало"]))
async def smth_else(message: Message):
    await message.answer(f"Ну, {message.from_user.first_name}, что посмотрим теперь? ",
                         reply_markup=cities)
