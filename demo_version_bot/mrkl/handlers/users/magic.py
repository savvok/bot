from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import magic, magic2, end_magic
from loader import dp


@dp.message_handler(Command("magic"))
async def ask_magic(message: Message):
    await message.answer("Я могу исполнить твоё желание", reply_markup=magic)


@dp.message_handler(Text(equals=["Закрыть лабы", "Поесть", "Поспать"]))
async def give_magic(message: Message):
    await message.answer(f"{message.text}? Твоё желание скоро будет исполнено!", reply_markup=end_magic)

@dp.message_handler(Text(equals=["Исполнить другое желание"]))
async def give_other_magic(message: Message):
    await message.answer(f"Ладно, а у тебя есть желание получше?", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Ты можешь выбрать любое", reply_markup=magic2)

@dp.message_handler(Text(equals=["Пока хватит"]))
async def smth_else2(message: Message):
    await message.answer(f"Как пожелаешь, {message.from_user.first_name}", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Попросить ещё"]))
async def smth_else(message: Message):
    await message.answer(f"Ну, {message.from_user.first_name}, что ещё ты желаешь?", reply_markup=magic)
