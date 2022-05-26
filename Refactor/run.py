import telebot
from loguru import logger

bot = telebot.TeleBot('5112938364:AAHI0bp5-KL4wqLpozfY_YLlErpw6RwDExQ')


def on_startup(bot: telebot.TeleBot):

    import filters

    filters.setup(bot)


# Now, you can use it in handler.
# @bot.message_handler(is_private=True)
# def private_message(message):
#  bot.send_message(message.chat.id, 'You get message in pm!')


if __name__ == '__main__':

    from handlers import bot

    on_startup(bot=bot)

    bot.polling(none_stop=True, interval=0)

    try:

        bot.polling(none_stop=True)

    except Exception as e:

        logger.exception("Fail startup:", e)
