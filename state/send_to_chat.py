from aiogram.dispatcher.filters.state import StatesGroup, State


# Отправка заявки от пользователя
class send_news_admin(StatesGroup):
    text = State()
    state = State()
    photo = State()