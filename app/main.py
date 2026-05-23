from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers.basic_handlers import basic_router
from app.handlers.menu_handlers import menu_router
from app.handlers.navigation_handlers import navigation_router
from app.handlers.services_handlers import services_router
from app.handlers.faq_handlers import faq_router
from app.handlers.fsm_handlers import fsm_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(basic_router)
    dp.include_router(fsm_router)
    dp.include_router(menu_router)
    dp.include_router(services_router)
    dp.include_router(navigation_router)
    dp.include_router(faq_router)

    print('Start...')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
