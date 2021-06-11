from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cities = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Санкт-Петербург"),
        ],
        [
            KeyboardButton(text="Москва (тусит)"),
            KeyboardButton(text="Саратов (шутка)")
        ],
        [
            KeyboardButton(text="Другой город (скоро)"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)

