from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка отменить
kb_cancel = InlineKeyboardMarkup(row_width=1)
btn_cancel = InlineKeyboardButton(text='❌Отменить', callback_data='quit')
kb_cancel.add(btn_cancel)

# Кнопки меню выбора перед отправкой
kb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📷Добавить фото', callback_data='add_photo'),
                                        InlineKeyboardButton(text='⬆Отправить', callback_data='next'),
                                        InlineKeyboardButton(text='❌Отменить', callback_data='quit')

                                    ]
                                ])

# Кнопки меню отправки фото
kb_menu_photo = InlineKeyboardMarkup(row_width=1)
btn_photo_send = InlineKeyboardButton(text='⬆Отправить', callback_data='next')
btn_photo_cancel = InlineKeyboardButton(text='❌Отменить', callback_data='quit')
kb_menu_photo.add(btn_photo_send, btn_photo_cancel)
