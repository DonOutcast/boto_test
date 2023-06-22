from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from callback_data import (
    answer_callback,
    next_callback,
    preview_callback,
)


def get_question_keyboard(prev_question: int, next_question: int, answers: list[str]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for answer in answers:
        label = answer
        markup.insert(
            InlineKeyboardButton(
                text=answer,
                callback_data=answer_callback.new(user_answer=answer),
            )
        )
    markup.row(
        InlineKeyboardButton(
            text="Назад ↩",
            callback_data=preview_callback.new(question_=prev_question)
        ),
        InlineKeyboardButton(
            text="Результа 📋",
            callback_data="result"
        ),
        InlineKeyboardButton(
            text="Вперед ↪",
            callback_data=next_callback.new(question_=next_question)
        )
    )
    return markup


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
