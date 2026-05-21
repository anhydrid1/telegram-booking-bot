from aiogram import Router, F
from aiogram.types import CallbackQuery
import app.keyboards.services_keydoard as kb
import app.keyboards.back_keyboard as kb_back
import app.keyboards.faq_keyboard as kb_faq

menu_router = Router()


@menu_router.callback_query(F.data == 'signin')
async def signin_cmd(callback: CallbackQuery):
    await callback.answer('Запись')


@menu_router.callback_query(F.data == 'services')
async def services_cmd(callback: CallbackQuery):
    await callback.answer('Услуги')
    await callback.message.edit_text('<b>Список доступных услуг</b>',
                                  parse_mode='HTML',
                                  reply_markup=kb.services_kb)


@menu_router.callback_query(F.data == 'contacts')
async def contacts_cmd(callback: CallbackQuery):
    await callback.answer('Контакты')
    await callback.message.edit_text('<b>Наши контакты</b>\n\n'
                                     'Тел.: +79652678965\n'
                                     'Почта: krutoysalon@gmail.com',
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_kb
                                     )


@menu_router.callback_query(F.data == 'faq')
async def faq_cmd(callback: CallbackQuery):
    await callback.answer('FAQ')
    await callback.message.edit_text('<b>Часто задаваемые вопросы</b>',
                                     parse_mode='HTML',
                                     reply_markup=kb_faq.faq_kb)
