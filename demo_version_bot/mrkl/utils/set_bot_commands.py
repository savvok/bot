from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Проснуться"),
        types.BotCommand("help", "Пояснить"),
        types.BotCommand("magic", "Поколдовать"),
        types.BotCommand("vuz_list", "Список вузов"),
        types.BotCommand("sleep", "Уснуть"),
    ])
