from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_for_c = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подтверждаю')],
    [KeyboardButton(text='Отмена')]
],
    resize_keyboard=True)
