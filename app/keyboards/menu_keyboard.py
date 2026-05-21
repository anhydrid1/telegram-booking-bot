from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📅 Записаться', callback_data='signin')],
    [InlineKeyboardButton(text='ℹ️ Услуги', callback_data='services')],
    [InlineKeyboardButton(text='📍Контакты', callback_data='contacts')],
    [InlineKeyboardButton(text='❓FAQ', callback_data='faq')]
])