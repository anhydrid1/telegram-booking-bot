from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]
])

back_faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_faq')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='back_home')]
])