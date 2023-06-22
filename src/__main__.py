from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging.config
from config import config
from keyboards import (
    back_to_menu,
    menu_markup,
    get_question_keyboard,
)

from callback_data import (
    next_callback,
    preview_callback,
)
from utils import add_sub
from log import LOGGING_CONFIG

bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=MemoryStorage())
logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("")

QUESTIONS = {
    0: {"Как ты?": ["Норм", "Пойдет", "Сам как"]},
    1: {"Кто ты воин?": ["Самурай", "Россамаха", "Человек-паук"]},
    2: {"Куда ты воин?": ["Домой", "Работать", "Похать"]},
}


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text="Добро пожаловть здесь ты можешь пройти опрос",
        reply_markup=menu_markup,
    )


@dp.message_handler(lambda message: "Начать опрос 📝" in message.text)
async def start_questions(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text=list(QUESTIONS.get(0).keys())[0],
        reply_markup=get_question_keyboard(0, 1, ["Норм", "Пойдет", "Сам как"])
    )


@dp.callback_query_handler(next_callback.filter())
async def next_(call: types.CallbackQuery, callback_data: dict):
    current_question = int(callback_data.get("question_"))
    try:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=list(QUESTIONS.get(current_question).keys())[0],
            reply_markup=get_question_keyboard(
                add_sub(current_question - 1),
                add_sub(current_question + 1),
                list(QUESTIONS.get(current_question).values())[0]
            )
        )
    except:
        pass


@dp.callback_query_handler(preview_callback.filter())
async def prev_(call: types.CallbackQuery, callback_data: dict):
    current_question = int(callback_data.get("question_"))
    try:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=list(QUESTIONS.get(current_question).keys())[0],
            reply_markup=get_question_keyboard(
                add_sub(current_question - 1),
                add_sub(current_question + 1),
                list(QUESTIONS.get(current_question).values())[0]
            )
        )
    except:
        pass


@dp.message_handler(lambda message: "Вернуться в главное меню 📜" in message.text)
async def cmd_cancel_registration(message: types.Message, state: FSMContext):
    await message.delete()
    try:
        await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
    except:
        pass
    current_state = await state.get_state()
    if current_state is None:
        await message.answer('Вы вернулись в главное меню', reply_markup=menu_markup)
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")
        return
    await state.finish()
    await message.answer('Вы вернулись в главное меню', reply_markup=menu_markup)
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")


def get_handled_updates_list(dp: Dispatcher) -> list:
    available_updates = (
        "callback_query_handlers", "channel_post_handlers", "chat_member_handlers",
        "chosen_inline_result_handlers", "edited_channel_post_handlers", "edited_message_handlers",
        "inline_query_handlers", "message_handlers", "my_chat_member_handlers", "poll_answer_handlers",
        "poll_handlers", "pre_checkout_query_handlers", "shipping_query_handlers"
    )
    return [item.replace("_handlers", "") for item in available_updates
            if len(dp.__getattribute__(item).handlers) > 0]


if __name__ == '__main__':
    logging.info("Бот запущен")
    executor.start_polling(dp, skip_updates=True, allowed_updates=get_handled_updates_list(dp))
    logging.info("Бот завершил свою работу")
