from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

end_magic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Попросить ещё"),
            KeyboardButton("Пока хватит")
        ]
    ])
