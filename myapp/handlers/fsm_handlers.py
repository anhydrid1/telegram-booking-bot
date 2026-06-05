from aiogram import Router, F
from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

import myapp.keyboards.services_kb_for_fsm_for_c as fsm_kb_for_c
import myapp.keyboards.services_kb_for_fsm as fsm_kb_service
import myapp.keyboards.menu_keyboard as menu_keyboard
import myapp.keyboards.date_keyboard as date_kb
import myapp.keyboards.time_keyboard as time_kb
from myapp.database.db import async_session

from myapp.database.models import Booking, Service
from sqlalchemy import select
from myapp.database.models import User

from myapp.states.fsm_signin import Reg
from aiogram.fsm.context import FSMContext

from datetime import datetime

fsm_router = Router()

# Выбор услуги
@fsm_router.callback_query(F.data == 'signin')
async def reg_one(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.service)
    await callback.answer('Вы выбрали запись')

    await callback.message.answer('Выберите доступную услугу',
                         reply_markup=fsm_kb_service.fsm_kb_signin)

# Выбор даты
@fsm_router.message(Reg.service)
async def reg_two(message: types.Message, state: FSMContext):
    await state.update_data(service=message.text)
    await state.set_state(Reg.data_t)
    await message.answer('Выберите свободную дату',
                         reply_markup=date_kb.date_keyboard)

# Выбор времени
@fsm_router.message(Reg.data_t)
async def reg_three(message: types.Message, state: FSMContext):
    await state.update_data(data_t=message.text)
    await state.set_state(Reg.time)
    await message.answer('Выберите свободное время',
                         reply_markup=time_kb.time_keyboard)

# Подтверждение
@fsm_router.message(Reg.time)
async def reg_four(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    await message.answer('Спасибо, запись почти завершена\n\n'
                         f'Услуга: {data['service']}\n'
                         f'Дата: {data['data_t']}\n'
                         f'Время: {data['time']}\n')

    await state.set_state(Reg.confirmation)
    await message.answer('Подтвердите запись',
                         reply_markup=fsm_kb_for_c.kb_for_c)


@fsm_router.message(Reg.confirmation)
async def reg_five(message: types.Message, state: FSMContext):
    await state.update_data(confirmation=message.text)

    if message.text == 'Подтверждаю':
        await message.answer('Спасибо за успешную запись!',
                            reply_markup=ReplyKeyboardRemove())

        await message.answer('Главное меню',
                            reply_markup=menu_keyboard.menu_kb)

        data = await state.get_data()

# Добавление записи в БД
        async with async_session() as session:

            result = await session.execute(
                select(User).where(
                    User.tg_id == message.from_user.id
                )
            )

            user = result.scalar_one()

            result2 = await session.execute(
                select(Service).where(
                    Service.name == data["service"]
                )
            )

            book_date = datetime.strptime(data['data_t'], "%d-%m-%Y").date()
            book_time = datetime.strptime(data['time'], "%H:%M").time()

            service = result2.scalar_one_or_none()

            booking = Booking(
                user_id=user.id,
                service_id=service.id,
                booking_date=book_date,
                booking_time=book_time
            )

            session.add(booking)

            await session.commit()

    elif message.text == 'Отмена':
        await message.answer('Запись не подтверждена',
                            reply_markup=ReplyKeyboardRemove())

        await message.answer('Главное меню',
                             reply_markup=menu_keyboard.menu_kb)

    await state.clear()
