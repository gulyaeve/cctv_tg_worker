import logging

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.enums import ParseMode

from bot.settings import settings

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Объект бота
if settings.TELEGRAM_API_SERVER:
    # Настройка сессии на кастомный api server
    session = AiohttpSession(api=TelegramAPIServer.from_base(settings.api_server_url, is_local=True))
    bot = Bot(
    token=settings.TELEGRAM_API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=session,
    )
elif settings.PROXY_URL:
    session = AiohttpSession(
        api=TelegramAPIServer.from_base(settings.api_server_url, is_local=True),
        proxy=(settings.PROXY_URL, settings.PROXY_SECRET)
    )
    bot = Bot(
        token=settings.TELEGRAM_API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=session,
    )
else:
    bot = Bot(
        token=settings.TELEGRAM_API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )


