from aiogram import Router, F
from aiogram.types import CallbackQuery
import myapp.keyboards.menu_keyboard as kb
import myapp.keyboards.faq_keyboard as kb_faq

navigation_router = Router()

# Хэндлер для возвращения назад после нажатия одной из кнопок в меню
@navigation_router.callback_query(F.data == 'back')
async def back_cmd(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.edit_text('<b>Главное меню</b>',
                                    parse_mode='HTML',
                                    reply_markup=kb.menu_kb)

# Хэндлер для возвращения назад
# FAQ -> Тип вопроса <--> Ответы на вопросы по типу
@navigation_router.callback_query(F.data == 'back_faq')
async def back_faq_cmd(callback: CallbackQuery):
    await callback.answer('Назад')
    await callback.message.edit_text('<b>Часто задаваемые вопросы</b>',
                                     parse_mode='HTML',
                                     reply_markup=kb_faq.faq_kb)

# Хэндлер для возвращения в главное меню: Ответы на тип вопроса -> Главное меню
@navigation_router.callback_query(F.data == 'back_home')
async def back_home_cmd(callback: CallbackQuery):
    await callback.answer('Главное меню')
    await callback.message.edit_text('<b>Главное меню</b>',
                                    parse_mode='HTML',
                                    reply_markup=kb.menu_kb)