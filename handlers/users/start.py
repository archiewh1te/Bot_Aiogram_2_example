import aiofiles as aiofiles
from aiogram import types
from filters import IsPrivate
from loader import dp
from utils.db_api import users_commands as commands
from utils.misc import rate_limit


# Функция по команде /start
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        # Проверка если пользователь есть в БД
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'✋ Приветствую тебя @<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!\n'
                                 f"🤖Я Бот Пример написанный на фреймворке AioGram 2\n"
                                 f"🌐GitHub моего создателя - https://github.com/archiewh1te\n"
                                 f"✍Если вы хотите заказать бота обратитесь к @ArchieWh1te")
    except Exception:
        # Добавление пользователя в БД
        await message.answer('Вы зарегистрированы ! Используйте команды:\n'
                             '/start\n'
                             '/sendnews\n'
                             '/about\n')
        await commands.add_users(user_id=message.from_user.id,
                             first_name=message.from_user.first_name,
                             last_name=message.from_user.last_name,
                             user_name=message.from_user.username,
                             status='active')
        # Запись в логи
    async with aiofiles.open(file='logs.txt', mode='a+', encoding='utf-8') as file:
        await file.write(
            f'Дата: {message.date} ChatId: {message.chat.id} и UserId: {message.from_user.id} '
            f'Юзернейм: {message.from_user.username} Сообщение: {message.text}\n')

