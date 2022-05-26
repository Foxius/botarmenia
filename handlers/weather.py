from ...run import bot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from telebot.types import ReplyKeyboardRemove

# модуль конфигов
config_dict = get_default_config()
owm = OWM('d99de04f9c4d8f439d5149e9d7c689ff', config_dict)


@bot.message_handler(commands=['weather'])
def weather(message):
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
    text_weather = f"""В городе ***Ереван*** сейчас:
        *Температура*: `{str(t1)}°C`
        *Ощущается как*: `{str(t2)}°C`
        *Скорость ветра*: `{str(wi)}м/с`
        *Давление*: `{str(pr)} мм.рт.ст`
        *Влажность*: `{str(humi)}%`
        """		
    if dt == "clear sky":
        photo = open('WeatherPhoto/clear sky.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "broken clouds":
        photo = open('WeatherPhoto/broken cloud.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "scattered clouds":
        photo = open('WeatherPhoto/broken cloud.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "few clouds":
        photo = open('WeatherPhoto/few clouds.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "shower rain":
        photo = open('WeatherPhoto/shower rain.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "rain":
        photo = open('WeatherPhoto/rain.png', 'rb')
        bot.send_document(message.chat.id, photo, caption=text_weather,
                          parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "thunderstorm":
        photo = open('WeatherPhoto/thunderstorm.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "snow":
        photo = open('WeatherPhoto/snow.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())
    if dt == "	mist":
        photo = open('WeatherPhoto/mist.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=text_weather,
                       parse_mode="Markdown", reply_markup=ReplyKeyboardRemove())