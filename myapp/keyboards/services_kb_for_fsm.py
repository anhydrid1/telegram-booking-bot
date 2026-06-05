from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fsm_kb_signin = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(text="Стрижка"), KeyboardButton(text="Маникюр")],
    [KeyboardButton(text="Массаж"), KeyboardButton(text="Консультация")]

],
    resize_keyboard=True )