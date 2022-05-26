from loguru import logger
from telebot import Telebot
from filters.pm import IsPrivate


def setup(bot: Telebot):
    logger.info('Connect filters...')
    bot.add_custom_filter(IsPrivate())


__all__ = ["setup"]
