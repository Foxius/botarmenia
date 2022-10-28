from telebot import types
import telebot
import telebot.types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaPhoto
from config import *
import colorama
from colorama import Fore
from openpyxl import load_workbook
colorama.init()
wb = load_workbook('test.xlsx')
wb.active = 0
sheet = wb.active
bot = telebot.TeleBot(token)
class Data(object):
    def __init__(self) -> None:
        self.data:dict={}
        self.i_obj2=0
        self.i_obj1=0
    def add(self,data:dict) -> None:
        self.data.update(data)
    def obj(self,num):
        if num==1:self.i_obj1+=1
        else: self.i_obj2+=1
data:object=Data()

def keyboard(keyboard:list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    markup.add(*[KeyboardButton(x) for x in keyboard])
    return markup

@bot.message_handler(commands=['rentadd'])
def rentadd_start(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reuse = types.KeyboardButton('Вторичка')
    newhouse = types.KeyboardButton('Новостройка')
    keyboard.row(reuse, newhouse)
    house = types.KeyboardButton('Жилой дом')
    dacha = types.KeyboardButton('Дача')
    keyboard.row(house, dacha)
    msg=bot.send_message(message.chat.id, 'Хорошо, для начала выберите тип жилья', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_repair)
def rentadd_repair(message):
    data.add({'type': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    euro = types.KeyboardButton('Евро ремонт')
    design = types.KeyboardButton('Дизайнерский')
    soviet = types.KeyboardButton('Советский')
    keyboard.row(euro,design,soviet)
    msg=bot.send_message(message.chat.id, 'Выберите тип ремонта', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_district)
def rentadd_district(message):
    data.add({'repair': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton("Ачапняк")
    btn1 = types.KeyboardButton("Арабкир")
    btn2 = types.KeyboardButton("Аван")
    keyboard.row(btn, btn1, btn2)
    btn3 = types.KeyboardButton("Давташен")
    btn4 = types.KeyboardButton("Эребуни") 
    btn5 = types.KeyboardButton("Канакер-Зейтун")
    keyboard.row(btn3, btn4, btn5) 
    btn6 = types.KeyboardButton("Кентрон")  
    btn7 = types.KeyboardButton("Малатия-Себастия") 
    btn8 = types.KeyboardButton("Норк-Мараш")
    keyboard.row(btn6, btn7, btn8)
    btn9 = types.KeyboardButton("Нор-Норк") 
    btn10 = types.KeyboardButton("Нубарашен") 
    btn11 = types.KeyboardButton("Шенгавит")
    keyboard.row(btn9, btn10, btn11)
    msg = bot.send_message(message.chat.id, "Теперь выберите район", reply_markup = keyboard)
    bot.register_next_step_handler(msg, rentadd_metrs)
def rentadd_metrs(message):
    data.add({'district': message.text})
    msg = bot.send_message(message.chat.id, 'Введите размер квартиры в квадратных метрах')
    bot.register_next_step_handler(msg, rentadd_conditioner)
def rentadd_conditioner(message):
    data.add({'metrs': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes=types.KeyboardButton('Да')
    no=types.KeyboardButton('Нет') 
    keyboard.row(yes, no)
    msg = bot.send_message(message.chat.id, 'Есть ли у вас кондиционеры?', reply_markup = keyboard)
    bot.register_next_step_handler(msg, rentadd_conditioner_check)
def rentadd_conditioner_check(message):
    if message.text == 'Да':
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        one=types.KeyboardButton('Один')
        two=types.KeyboardButton('Два')
        three=types.KeyboardButton('Три')
        keyboard.row(one, two, three)
        some=types.KeyboardButton('4 и больше')
        keyboard.row(some)
        msg = bot.send_message(message.chat.id, 'Выберите количество кондиционеров', reply_markup = keyboard)
        bot.register_next_step_handler(msg, rentadd_heating_true)
    if message.text == 'Нет':
        data.add({'conditioner': '-'})
        rentadd_heating(message)
    else:
        bot.send_message(message.chat.id,'Произошла ошибка. перезапустите команду /rentadd заново')
def rentadd_heating_true(message):
    data.add({'conditioner': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes=types.KeyboardButton('Да')
    no=types.KeyboardButton('Нет') 
    keyboard.row(yes, no)
    msg = bot.send_message(message.chat.id, 'Есть ли у вас отопительные системы?', reply_markup = keyboard)
    bot.register_next_step_handler(msg, rentadd_heating_check)
def rentadd_heating(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes=types.KeyboardButton('Да')
    no=types.KeyboardButton('Нет') 
    keyboard.row(yes, no)
    msg = bot.send_message(message.chat.id, 'Есть ли у вас отопительные системы?', reply_markup = keyboard)
    bot.register_next_step_handler(msg, rentadd_heating_check)
def rentadd_heating_check(message):
    if message.text == 'Да':
        msg = bot.send_message(message.chat.id, 'Что за система у вас стоит?')
        bot.register_next_step_handler(msg, rentadd_animals_true)
    if message.text == 'Нет':
        data.add({'heating': '-'})
        rentadd_animals(message)
    else:
        bot.send_message(message.chat.id,'Произошла ошибка. перезапустите команду /rentadd заново')
def rentadd_animals(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    positive = types.KeyboardButton('Позитивное')
    calm = types.KeyboardButton('Спокойное')
    keyboard.row(positive, calm)
    neutral = types.KeyboardButton('Нейтральное')
    keyboard.row(neutral)
    undesirable = types.KeyboardButton('Нежелательное')
    negative = types.KeyboardButton("Негативное")
    keyboard.row(undesirable, negative)
    msg = bot.send_message(message.chat.id, 'Выберите ваше отношение к животным в квартире', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_rooms)
def rentadd_animals_true(message):
    data.add({'heating': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    positive = types.KeyboardButton('Позитивное')
    calm = types.KeyboardButton('Спокойное')
    keyboard.row(positive, calm)
    neutral = types.KeyboardButton('Нейтральное')
    keyboard.row(neutral)
    undesirable = types.KeyboardButton('Нежелательное')
    negative = types.KeyboardButton("Негативное")
    keyboard.row(undesirable, negative)
    msg = bot.send_message(message.chat.id, 'Выберите ваше отношение к животным в квартире', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_rooms)
def rentadd_rooms(message):
    data.add({'animals': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   
    room1=types.KeyboardButton('1 комната')
    room2=types.KeyboardButton('2 комнаты')
    room3=types.KeyboardButton('3 комнаты')
    room4=types.KeyboardButton('4 комнаты')
    keyboard.row(room1, room2, room3, room4)
    roomsome=types.KeyboardButton('Более 4 комнат')
    keyboard.row(roomsome)
    msg = bot.send_message(message.chat.id, f'Выберите количество комнат', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_layers)
def rentadd_layers(message):
    data.add({'rooms': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   
    layer1=types.KeyboardButton('1 этаж')
    layer2=types.KeyboardButton('2 этаж')
    layer3=types.KeyboardButton('3 этаж')
    layer4=types.KeyboardButton('4 этаж')
    keyboard.row(layer1, layer2, layer3, layer4)
    layersome=types.KeyboardButton('5 этаж и выше') 
    bot.register_next_step_handler(bot.send_message(message.chat.id, f'Выберите этаж', reply_markup=keyboard), rentadd_tech)
def rentadd_tech(message):
    data.add({'layer': message.text})
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Расскажите подробнее о бытовой технике которая находится'), rentadd_period)
def rentadd_period(message):
    data.add({'tech': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    month1 = types.KeyboardButton('До 1 месяца')
    month3 = types.KeyboardButton('От 1 до 3 месяцев')
    keyboard.row(month1, month3)
    month6 = types.KeyboardButton('От 3 до 6 месяцев')
    keyboard.row(month6)
    monthsome= types.KeyboardButton('Более 6 месяцев')
    keyboard.row(monthsome)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Выберите период сдачи квартиры', reply_markup=keyboard), rentadd_cost)
def rentadd_cost(message):
    data.add({'period': message.text})
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Введите стоимость в месяц (в драмах **ТОЛЬКО ЧИСЛО БЕЗ ТОЧЕК, ПРОБЕЛОВ, ЗАПЯТЫХ**)', parse_mode='Markdown'), rentadd_phone)
def rentadd_phone(message):
    data.add({'cost': message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    keyboard.row(yes,no)
    msg = bot.send_message(message.chat.id, 'Следующим действием я запрошу ваш номер для связи с вами, если вы не хотите давать номер вашего телеграмм аккаунта или не хотите связи по телефону, нажмите нет. Иначе - нажмите да', reply_markup=keyboard)
    bot.register_next_step_handler(msg, rentadd_phone_check)
def rentadd_phone_check(message):
    if message.text == 'Да':
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
        keyboard.add(button_phone)
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Нажмите на кнопку ниже', reply_markup=keyboard), rentadd_photo)
    if message.text == 'Нет':
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хорошо. Отправьте другой номер для связи, или же отправьте прочерк (-)'), rentadd_photo)
def rentadd_photo(message):
    if message.contact is not None:
        data.add({'phone':message.contact.phone_number})
    else:
        data.add({'phone':message.text})
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    keyboard.row(yes,no)
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хотите ли вы добавить фото?', reply_markup=keyboard), file_obj1)
def file_obj1(message):
    if message.text=='Нет':
        bot.register_next_step_handler(bot.send_message(message.chat.id, f'Введите комментарий/описание квартиры'),rentadd_comment)
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, f'Отправте файл'),rentadd_photo_obj1)
def rentadd_photo_obj1(message):
    if not data.i_obj1:data.add({'obj1': [{'files': [bot.download_file(bot.get_file(message.photo[1].file_id).file_path)]}]})
    else:data.data['obj1'][0]['files'].append(bot.download_file(bot.get_file(message.photo[1].file_id).file_path))
    data.obj(1)
    bot.register_next_step_handler(bot.send_message(message.chat.id, f'Добавить еще один файл?', reply_markup=keyboard(['Да','Нет'])), file_obj1)
def rentadd_comment(message):
    data.data['obj1'][0].update({'comment': message.text})
    if not data.i_obj1:
        bot.send_message(message.chat.id, f"""
            Подтвердите объявление:

            Тип жилья: {data.data['type']}
            Тип ремонта: {data.data['repair']}
            Район: {data.data['district']}
            Размер квартиры: {data.data['metrs']}
            Количество кондиционеров: {data.data['conditioner']}
            Отопительная система: {data.data['heating']}
            Отношение к животным: {data.data['animals']}
            Количество комнат: {data.data['rooms']}
            Этаж: {data.data['layer']}
            Наличие бытовой техники: {data.data['tech']}
            Период сдачи: {data.data['period']}
            Стоимость в месяц: {data.data['cost']}
            Комментарий от владельца: {data.data["obj1"][0]["comment"]}
            ТГ аккаунт для связи: @{message.from_user.username}
            Номер для связи: {data.data['phone']}
            """)
    if data.i_obj1:
            bot.send_media_group(message.chat.id, [InputMediaPhoto(data.data["obj1"][0]["files"][i], caption=f"""
            Подтвердите объявление:

            Тип жилья: {data.data['type']}
            Тип ремонта: {data.data['repair']}
            Район: {data.data['district']}
            Размер квартиры: {data.data['metrs']}
            Количество кондиционеров: {data.data['conditioner']}
            Отопительная система: {data.data['heating']}
            Отношение к животным: {data.data['animals']}
            Количество комнат: {data.data['rooms']}
            Этаж: {data.data['layer']}
            Наличие бытовой техники: {data.data['tech']}
            Период сдачи: {data.data['period']}
            Стоимость в месяц: {data.data['cost']}
            Комментарий от владельца: {data.data["obj1"][0]["comment"]}
            ТГ аккаунт для связи: @{message.from_user.username}
            Номер для связи: {data.data['phone']}
            """) if not i else InputMediaPhoto(data.data["obj1"][0]["files"][i]) for i in range(len(data.data["obj1"][0]["files"]))])
   

 




def rentadd_confirm():
    pass


bot.polling()