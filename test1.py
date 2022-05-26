import telebot
import config
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import emoji
from telebot import types
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# модуль конфигов
config_dict = get_default_config()
owm = OWM('d99de04f9c4d8f439d5149e9d7c689ff', config_dict)
bot = telebot.TeleBot('5112938364:AAHI0bp5-KL4wqLpozfY_YLlErpw6RwDExQ')
moderchatid = '-1001680279204'

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Добро Пожаловать", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['weather'])
def weather(message):
	config_dict = get_default_config()
	owm = OWM('d99de04f9c4d8f439d5149e9d7c689ff', config_dict)
	place = 'Ереван'
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(place)
	w = observation.weather
	t = w.temperature("celsius")
	t1 = t['temp']
	t2 = t['feels_like']
	t3 = t['temp_max']
	t4 = t['temp_min']

	wi = w.wind()['speed']
	humi = w.humidity
	cl = w.clouds
	st = w.status
	dt = w.detailed_status
	ti = w.reference_time('iso')
	pr = w.pressure['press']
	vd = w.visibility_distance

	press = int(pr) * float("0.75")

	textweather = f"""В городе ***Ереван*** сейчас:
		*Температура*: `{str(t1)}°C`
		*Ощущается как*: `{str(t2)}°C`
		*Скорость ветра*: `{str(wi)}м/с`
		*Давление*: `{str(press)} мм.рт.ст`
		*Влажность*: `{str(humi)}%`
		{dt}
		"""		
	print(textweather)

	if dt == "clear sky":
		photo = open('WeatherPhoto/clear sky.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "broken clouds":
		photo = open('WeatherPhoto/broken cloud.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "scattered clouds":
		photo = open('WeatherPhoto/broken cloud.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "few clouds":
		photo = open('WeatherPhoto/few clouds.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "shower rain":
		photo = open('WeatherPhoto/shower rain.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "rain":
		photo = open('WeatherPhoto/rain.png', 'rb')
		bot.send_document(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "thunderstorm":
		photo = open('WeatherPhoto/thunderstorm.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "snow":
		photo = open('WeatherPhoto/snow.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
	if dt == "mist":
		photo = open('WeatherPhoto/mist.png', 'rb')
		bot.send_photo(message.chat.id, photo, caption=textweather, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True, interval=0)
