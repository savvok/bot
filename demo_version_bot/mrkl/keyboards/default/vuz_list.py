from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# vuzlist = list(range(1,32))
vuzes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Университет ИТМО"),
        ],
        [
            KeyboardButton(text="СПБГУ"),
            KeyboardButton(text="ВШЭ"),
        ],
        [
            KeyboardButton(text="Политех"),
            KeyboardButton(text="Бонч"),
        ],
        [
            KeyboardButton(text="Страшно вырубай"),
        ]
    ],
    resize_keyboard=True
)
