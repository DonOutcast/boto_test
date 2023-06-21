from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionState(StatesGroup):
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()

