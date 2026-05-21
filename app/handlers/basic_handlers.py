from aiogram import types, Router
from aiogram.filters.command import Command
import app.keyboards.menu_keyboard as kb

basic_router = Router()

@basic_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'<b>Здравствуйте</b>, {message.from_user.full_name}!\n'
                         '<b>Добро пожаловать в наш салон!</b>\n\n'
                         '<i>Для того, чтобы записаться или посмотреть список услуг, воспользуйтесь главным меню</i>',
                         parse_mode='HTML')

    await message.answer('<b>Главное меню</b>',
                         parse_mode='HTML',
                         reply_markup=kb.menu_kb)

