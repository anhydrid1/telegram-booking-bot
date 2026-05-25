from aiogram import Router, F
from aiogram.types import CallbackQuery

services_router = Router()

# Хэндлер для обработки нажатия, на тип услуги - стрижка
@services_router.callback_query(F.data == 'hair')
async def hair_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали стрижки')

# Хэндлер для обработки нажатия, на тип услуги - маникюр
@services_router.callback_query(F.data == 'manicure')
async def manicure_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали маникюр')

# Хэндлер для обработки нажатия, на тип услуги - массаж
@services_router.callback_query(F.data == 'massage')
async def massage_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали массаж')

# Хэндлер для обработки нажатия, на тип услуги - консультация
@services_router.callback_query(F.data == 'consultation')
async def consultation_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали консультацию')

