from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext

from config import config
# Please, keep your bot tokens on environments, this code only example
bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message, state: FSMContext) -> None:
    await message.answer(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
