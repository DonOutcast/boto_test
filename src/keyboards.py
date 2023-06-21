from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
back_to_menu = ReplyKeyboardMarkup(resize_keyboard=True)
back_to_menu.add(
    KeyboardButton(
        "Вернуться в главное меню 📜"
    )
)
menu_markup.add(
    KeyboardButton(
        "Начать опрос 📝"
    )
)
options = ['Вариант 1', 'Вариант 2', 'Вариант 3']
polls_markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
polls_markup.add(*options)

