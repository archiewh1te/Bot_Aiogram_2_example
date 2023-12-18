from aiogram import types
from aiogram.dispatcher import FSMContext
from filters import IsPrivate, IsAdminCheck
from keyboards.inline import kb_cancel, kb_menu_photo, kb_menu
from loader import dp
from state.send_to_chat import send_news_admin
from data.config import cfg

chanel_id = cfg['channel_ids']


# Отправка уведомления для всех пользователей
@dp.message_handler(IsPrivate(), IsAdminCheck(), text="/sendnews")
async def get_send_notice(message: types.Message):
    global msg_answer
    msg_answer = await message.answer(f'Введите текст для отправки в группу:', reply_markup=kb_cancel)
    await send_news_admin.text.set()


@dp.message_handler(IsPrivate(), state=send_news_admin)
async def notice_text(message: types.Message, state: FSMContext):
    await message.delete()
    answer = message.text
    await state.update_data(text=answer)
    await message.answer(text=f'<b>Вы написали</b>: {answer}', reply_markup=kb_menu)
    await send_news_admin.state.set()
    await msg_answer.delete()


@dp.callback_query_handler(text='next', state=send_news_admin.state)
async def start_notice(call: types.CallbackQuery, state:FSMContext):
    await call.answer(cache_time=5)
    await call.message.delete()
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    await dp.bot.send_message(chanel_id, text=f"📩 Уведомление от Администратора:\n"
                                                                           f"<b>{text}</b>")
    await call.message.answer('✉ Ваша новость была отослана в группу.')


@dp.callback_query_handler(text='add_photo', state=send_news_admin.state)
async def add_photo(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.delete()
    global msg_photo_answer
    msg_photo_answer = await call.message.answer('Пришлите фото')
    await send_news_admin.photo.set()


@dp.message_handler(IsPrivate(), state=send_news_admin.photo, content_types=types.ContentType.PHOTO)
async def send_text(message: types.Message, state: FSMContext):
    await msg_photo_answer.delete()
    await message.delete()
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await message.answer_photo(photo=photo, caption=f'<b>Вы написали</b>: {text}\n'
                                                    f'И прикрепили фото, теперь нажмите кнопку ⬆Отправить', reply_markup=kb_menu_photo)


@dp.callback_query_handler(text='next', state=send_news_admin.photo)
async def get_start_notice(call: types.CallbackQuery, state:FSMContext):
    await call.answer(cache_time=5)
    await call.message.delete()
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    await dp.bot.send_photo(chanel_id, photo=photo, caption=f"📩 Уведомление от Администратора:\n"
                                                                                                f"<b>{text}</b>")
    await call.message.answer('✉ Ваша новость была отослана в группу.')


@dp.message_handler(IsPrivate(), state=send_news_admin.photo)
async def no_photo(message: types.Message):
    await message.answer('Пришли мне фото', reply_markup=kb_cancel)


@dp.callback_query_handler(text='quit', state=[send_news_admin.text, send_news_admin.photo, send_news_admin.state])
async def quit(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await state.finish()
    await call.message.delete()
    await call.message.answer('❌Отправка новости в группу отменена')




