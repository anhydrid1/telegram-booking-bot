from aiogram import types, Router
from aiogram.filters.command import Command
import myapp.keyboards.menu_keyboard as kb

from sqlalchemy import select

from myapp.database.db import async_session
from myapp.database.models import User

basic_router = Router()

# Начальная команда при запуске бота
@basic_router.message(Command('start'))
async def start_cmd(message: types.Message):

    async with async_session() as session:

        result = await session.execute(
            select(User).where(
                User.tg_id == message.from_user.id
            )
        )

        user = result.scalar_one_or_none()

        if user is None:

            user = User(
                tg_id=message.from_user.id,
                username=message.from_user.username
            )

            session.add(user)

            await session.commit()

    await message.answer(f'<b>Здравствуйте</b>, {message.from_user.full_name}!\n'
                         '<b>Добро пожаловать в наш салон!</b>\n\n'
                         '<i>Для того, чтобы записаться или посмотреть список услуг, воспользуйтесь главным меню</i>',
                         parse_mode='HTML')

    await message.answer('<b>Главное меню</b>',
                         parse_mode='HTML',
                         reply_markup=kb.menu_kb)
