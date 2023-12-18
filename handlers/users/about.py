from aiogram import types

from filters import IsPrivate
from loader import dp

from utils.misc import rate_limit


# Функция по команде /about
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/about')
async def command_start(message: types.Message):
    await message.answer(f"🤖Я - Бот явлюящийся болванкой\n"
                         f"👤Owner: @ArchieWh1te\n"
                         f"🌐 Группа в TG - https://t.me/ArchieWh1teDev "
                         )