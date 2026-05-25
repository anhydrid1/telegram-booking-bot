from aiogram import Router, F
from aiogram.types import CallbackQuery
import myapp.keyboards.back_keyboard as kb_back

faq_router = Router()

# Хэндлер для faq для вопросов о записи и времени
@faq_router.callback_query(F.data == 'signin_time')
async def signin_time_cmd(callback: CallbackQuery):
    await callback.answer('Запись и время')

    text = ('❓ <b>Как записаться?</b>\n'
            'Нажмите «📅 Записаться», выберите услугу, дату и\n'
            'свободное время. Подтвердите запись — и мы вас ждём.\n\n'
            
            '❓ <b>Могу ли я записаться сегодня?</b>\n'
            'Да, если есть свободные окошки. Минимальный срок — за 2 часа до'
            'визита (чтобы мастер успел подготовиться).\n\n'
            
            '❓ <b>Как узнать свободное время?</b>\n'
            'Бот показывает только реально свободные слоты. Если время не\n'
            'отображается — оно занято.'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_faq_kb)

# Хэндлер для вопросов об услугах
@faq_router.callback_query(F.data == 'services_info')
async def services_info_cmd(callback: CallbackQuery):
    await callback.answer('Услуги')

    text = ('❓ <b>Сколько длится услуга?</b>\n'
            'Стрижка — 40–60 мин\n'
            'Маникюр — 60–90 мин\n'
            'Консультация — 20–30 мин\n\n'
            
            '❓ <b>Нужна ли предоплата?</b>\n'
            'Нет. Но если вы не приходите и не отменяете запись за 2 часа — мы'
            'будем вынуждены внести вас в «стоп-лист» на будущие записи.'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_faq_kb)

# Хэндлер для вопросов об опазданиях
@faq_router.callback_query(F.data == 'late')
async def late_cmd(callback: CallbackQuery):
    await callback.answer('Опоздания и неявки')

    text = ('❓ <b>Что будет, если я опоздаю?</b>\n'
            'Если опоздали на 5–10 минут — мастер вас примет, но процедура может'
            'быть сокращена.\n'
            'Если на 15+ минут без звонка — запись аннулируется, и вы попадаете в'
            'список «неявок».\n\n'
            
            '❓ <b>Что такое «неявка»?</b>\n'
            'Это когда клиент не пришёл и не предупредил. После 2 неявок бот'
            'заблокирует возможность записи через бота — только по телефону.'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_faq_kb)

# Хэндлер для вопросов о консультациях
@faq_router.callback_query(F.data == 'consultation_faq')
async def consultation_faq_cmd(callback: CallbackQuery):
    await callback.answer('Консультации и особые случаи')

    text = ('❓ <b>Что такое консультация и зачем она?</b>\n'
            'Короткая встреча с мастером (20–30 мин), чтобы подобрать стрижку,'
            'форму ногтей или уход.\n'
            'Или если вы сомневаетесь, нужна ли вам процедура.\n\n'
            
            '❓ <b>Можно ли с ребёнком?</b>\n'
            'Да, но ребёнок должен находиться рядом с вами. Отдельной детской'
            'стрижки пока нет (кроме детей 7+ лет).'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_faq_kb)

# Хэндлер для помощи
@faq_router.callback_query(F.data == 'help')
async def help_cmd(callback: CallbackQuery):
    await callback.answer('Помощь')

    text = ('❓ <b>Бот не работает / не могу записаться / ошибка</b>\n'
            'Напишите нам в телеграм: @support_salon (живой человек ответит с'
            '10:00 до 21:00) или позвоните +79652678965\n\n'
            
            '❓ <b>Где находится салон?</b>\n'
            'г.Севастопо, ул.Серова, д.6, этаж 3\n\n'
            
            '❓ <b>Как связаться с администратором напрямую?</b>\n'
            '@Admin — по любым вопросам, кроме записи (запись только через'
            'бота).'
            )

    await callback.message.edit_text(text,
                                     parse_mode='HTML',
                                     reply_markup=kb_back.back_faq_kb)