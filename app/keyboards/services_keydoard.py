from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

services_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💇‍♂️ Стрижка', callback_data='hair')],
    [InlineKeyboardButton(text='💅 Маникюр', callback_data='manicure')],
    [InlineKeyboardButton(text='💆‍♂️ Массаж', callback_data='massage')],
    [InlineKeyboardButton(text='📝 Консультация', callback_data='consultation')],
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]
])
