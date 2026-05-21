from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🗓 Запись и время', callback_data='signin_time')],
    [InlineKeyboardButton(text='💇‍♀️ Услуги', callback_data='services_info')],
    [InlineKeyboardButton(text='❌ Опоздания и неявки', callback_data='late')],
    [InlineKeyboardButton(text='💬 Консультации и особые случаи', callback_data='consultation_faq')],
    [InlineKeyboardButton(text='📞 Помощь', callback_data='help')],
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]
])
