from aiogram import Router, F
from aiogram.types import CallbackQuery
import app.keyboards.menu_keyboard as kb
import app.keyboards.faq_keyboard as kb_faq

navigation_router = Router()

@navigation_router.callback_query(F.data == 'back')
async def back_cmd(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.edit_text('<b>Главное меню</b>',
                                    parse_mode='HTML',
                                    reply_markup=kb.menu_kb)


@navigation_router.callback_query(F.data == 'back_faq')
async def back_faq_cmd(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.edit_text('<b>Часто задаваемые вопросы</b>',
                                     parse_mode='HTML',
                                     reply_markup=kb_faq.faq_kb)


@navigation_router.callback_query(F.data == 'back_home')
async def back_home_cmd(callback: CallbackQuery):
    await callback.answer('Главное меню')
    await callback.message.edit_text('<b>Главное меню</b>',
                                    parse_mode='HTML',
                                    reply_markup=kb.menu_kb)