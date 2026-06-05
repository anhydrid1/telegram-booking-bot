from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from sqlalchemy import select

from myapp.database.db import async_session
from myapp.database.models import User

users_router = Router()

# Добавление пользователя в БД
@users_router.message(CommandStart())
async def cmd_start(message: Message):

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