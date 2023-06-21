from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType

from config import config

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor

from keyboards import back_to_menu, menu_markup, polls_markup
from fsm import QuestionState

bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=MemoryStorage())

user_answers = {}


# Function to send a question with answer options as inline buttons
async def send_question(chat_id, question, options):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=option, callback_data=option) for option in options]
    markup.add(*buttons)
    await bot.send_message(chat_id, question, reply_markup=markup)


# Handler for the /start command
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    chat_id = message.chat.id
    question = "Привет! Начнем опрос. Какие цвета тебе нравятся?"
    options = ["Красный", "Зеленый", "Синий"]
    await send_question(chat_id, question, options)


# Handler for answer options
@dp.callback_query_handler()
async def handle_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    answer = callback_query.data

    # Get the previous question, the answer to which affects the current question
    prev_question = user_answers.get(chat_id)
    зкшт
    if prev_question == "Привет! Начнем опрос. Какие цвета тебе нравятся?":
        # Store multiple answers in a list
        user_answers[chat_id] = [answer]
        question = "Выбери фрукты:"
        options = ["Яблоко", "Апельсин", "Банан"]
        await send_question(chat_id, question, options)
    elif prev_question == "Выбери фрукты:":
        # Append the answer to the list of previous answers
        user_answers[chat_id].append(answer)
        question = "Выбери напитки:"
        options = ["Чай", "Кофе", "Сок"]
        await send_question(chat_id, question, options)
    else:
        # Handle the next question based on the answers
        pass
        # ...

    # Send a confirmation message for the selected answer
    await bot.answer_callback_query(callback_query.id, f"You selected: {answer}")


# Handler for the /results command
@dp.message_handler(commands=["results"])
async def results_command(message: types.Message):
    chat_id = message.chat.id
    answers = user_answers.get(chat_id)
    if answers:
        await bot.send_message(chat_id, f"Результаты опроса:\n{answers}")
    else:
        await bot.send_message(chat_id, "Опрос еще не завершен.")


# Handler for the /cancel command
@dp.message_handler(commands=["cancel"])
async def cancel_command(message: types.Message):
    chat_id = message.chat.id
    user_answers.pop(chat_id, None)
    await bot.send_message(chat_id, "Опрос отменен.")


# @dp.message_handler(commands=["start"])
# async def cmd_start(message: types.Message) -> None:
#     await message.answer(
#         text="Добро пожаловть здесь ты можешь пройти опрос",
#         reply_markup=menu_markup,
#     )
#
#
# @dp.message_handler(lambda message: "Начать опрос 📝" in message.text)
# async def question_1(message: types.Message, state: FSMContext) -> None:
#     await message.answer_poll(
#         question="Как ты",
#         options=["1", "2", "3", "4"],
#         allows_multiple_answers=True,
#         is_anonymous=False,
#     )
#     await QuestionState.answer_1.set()
#
#
# @dp.poll_answer_handler()
# async def poll_answers(poll_answer: types.PollAnswer):
#     print(poll_answer.option_ids, poll_answer.poll_id)
#     print(poll_answer.get_current())
#
#
#
# # @dp.poll_answer_handler(lambda poll: poll.is_closed)
# # async def cath_question_1(poll: types.PollAnswer):
# #     print(poll)
#
#
# @dp.message_handler(lambda message: "Вернуться в главное меню 📜" in message.text)
# async def cmd_cancel_registration(message: types.Message, state: FSMContext):
#     await message.delete()
#     try:
#         await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
#     except:
#         pass
#     current_state = await state.get_state()
#     if current_state is None:
#         await message.answer('Вы вернулись в главное меню', reply_markup=menu_markup)
#         await bot.send_sticker(message.from_user.id,
#                                sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")
#         return
#     await state.finish()
#     await message.answer('Вы вернулись в главное меню', reply_markup=menu_markup)
#     await bot.send_sticker(message.from_user.id,
#                            sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")


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
    executor.start_polling(dp, skip_updates=True, allowed_updates=get_handled_updates_list(dp))
