from aiogram import Router, F
from aiogram.types import CallbackQuery

services_router = Router()


@services_router.callback_query(F.data == 'hair')
async def hair_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали стрижки')


@services_router.callback_query(F.data == 'manicure')
async def manicure_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали маникюр')


@services_router.callback_query(F.data == 'massage')
async def massage_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали массаж')


@services_router.callback_query(F.data == 'consultation')
async def consultation_cmd(callback: CallbackQuery):
    await callback.answer('Вы выбрали консультацию')

