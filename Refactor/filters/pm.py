from telebot.types import Message
from telebot.custom_filters import SimpleCustomFilter


class IsPrivate(SimpleCustomFilter):
    key = 'is_private'

    @staticmethod
    def check(message: Message):
        return message.chat.type == "private"
