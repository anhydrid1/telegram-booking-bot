from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура, используемая для перехода на одно вложение назад(сразу в главное меню)
back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]
])

# Клавиатура, которая отображается в FAQ -> Типы вопросов ->
# Ответы на вопросы в соответсвии с типами
back_faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_faq')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='back_home')]
])
