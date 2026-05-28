from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from myapp.functions.gen_data import dates

date_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f'{dates[0]}'),KeyboardButton(text=f'{dates[1]}')],
    [KeyboardButton(text=f'{dates[2]}'),KeyboardButton(text=f'{dates[3]}')],
    [KeyboardButton(text=f'{dates[4]}'),KeyboardButton(text=f'{dates[5]}')],
    [KeyboardButton(text=f'{dates[6]}')]
],
    resize_keyboard=True)


