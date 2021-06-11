from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

magic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Закрыть лабы"),
        ],
        [
            KeyboardButton(text="Поспать"),
            KeyboardButton(text="Поесть")
        ],
        [
            KeyboardButton(text="Исполнить другое желание"),
        ]
    ],
    resize_keyboard=True
)

magic2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Закрыть лабы"),
        ],
        [
            KeyboardButton(text="Закрыть лабы"),
            KeyboardButton(text="Закрыть лабы"),
        ],
        [
            KeyboardButton(text="Закрыть лабы"),
        ]
    ],
    resize_keyboard=True
)
