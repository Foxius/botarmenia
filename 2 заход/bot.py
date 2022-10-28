import pyrogram
from pyrogram import Client
from pyrogram import filters
from rates import *
from pyowm import OWM
from config import *
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
bot = Client(
    "bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=token
)

print(Fore.RED + 'Бот запускается...')
print(Fore.BLUE + 'Добро пожаловать, капитан!')
@bot.on_message(filters.command('start'))
def welcome(bot, msg):
    print(Fore.YELLOW + 'Использована команда: start')
    bot.send_message(msg.chat.id, "Добро Пожаловать")
@bot.on_message(filters.command('rates'))
def rates(bot,msg):
    print(Fore.YELLOW + 'Использована команда: rates')
    bot.send_message(msg.chat.id, ratestext)
@bot.on_message(filters.command('weather'))
def weather(bot,msg):
    print(Fore.YELLOW + 'Использована команда: weather')
    owm = OWM(owmtoken)
    place = 'Ереван'
    mgr = owm.weather_manager()
    obseration = mgr.weather_at_place(place)
    w = obseration.weather
    t = w.temperature('celsius')
    t1 = t['temp']
    t2 = t['feels_like']
    wi = w.wind()['speed']
    pr = w.pressure['press']
    press = int(pr) * float("0.75")
    humi = w.humidity
    dt = w.detailed_status
    textweather = f"""В городе **Ереван** сейчас:
        **Температура**: `{str(t1)}°C`
        **Ощущается как**: `{str(t2)}°C`
        **Скорость ветра**: `{str(wi)}м/с`
        **Давление**: `{str(press)} мм.рт.ст`
        **Влажность**: `{str(humi)}%`
        """
    try:
        photo = open(f'WeatherPhoto/{str(dt)}.png', 'rb')
        bot.send_photo(msg.chat.id, photo, caption=textweather)
    except:
        photo = open(f'WeatherPhoto/maxresdefault.png', 'rb')
        bot.send_photo(msg.chat.id, photo, caption=textweather)
@bot.on_message(filters.command('faq'))
def faq(bot,msg):
    print(Fore.YELLOW + 'Использована команда: faq')
    bot.send_message(msg.chat.id, faqtext)

@bot.on_message(filters.command('help'))
def help(bot,msg):
    print(Fore.YELLOW + 'Использована команда: help')
    bot.send_message(msg.chat.id, f"""
    **Список команд**:

    **Полезная информация**
    ☀️ /weather - Текущая погода в Столице
    💲 /rates - Курсы покупки валюты в банках
    ❓ /faq - Часто задаваемые вопросы
    """)

bot.run()