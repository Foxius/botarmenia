from ...run import bot
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Добро Пожаловать", reply_markup=ReplyKeyboardRemove())
