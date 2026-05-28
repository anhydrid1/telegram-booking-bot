from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from myapp.functions.gen_time import slots_main

time_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f'{slots_main[0]}'), KeyboardButton(text=f'{slots_main[1]}')],
    [KeyboardButton(text=f'{slots_main[2]}'), KeyboardButton(text=f'{slots_main[3]}')],
    [KeyboardButton(text=f'{slots_main[4]}'), KeyboardButton(text=f'{slots_main[5]}')],
    [KeyboardButton(text=f'{slots_main[6]}'), KeyboardButton(text=f'{slots_main[7]}')]
],
    resize_keyboard=True)
