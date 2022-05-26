from ...run import bot
from openpyxl import load_workbook
from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


@bot.message_handler(commands=['rentflat'], is_private=True)
def rentflat(message: Message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton("Ачапняк")
    keyboard.add(btn)
    btn1 = KeyboardButton("Арабкир")
    keyboard.add(btn1)
    btn2 = KeyboardButton("Аван")
    keyboard.add(btn2)
    btn3 = KeyboardButton("Давташен")
    keyboard.add(btn3)
    btn4 = KeyboardButton("Эребуни")
    keyboard.add(btn4)
    btn5 = KeyboardButton("Канакер-Зейтун")
    keyboard.add(btn5)
    btn6 = KeyboardButton("Кентрон")
    keyboard.add(btn6)
    btn7 = KeyboardButton("Малатия-Себастия")
    keyboard.add(btn7)
    btn8 = KeyboardButton("Норк-Мараш")
    keyboard.add(btn8)
    btn9 = KeyboardButton("Нор-Норк")
    keyboard.add(btn9)
    btn10 = KeyboardButton("Нубарашен")
    keyboard.add(btn10)
    btn11 = KeyboardButton("Шенгавит")
    keyboard.add(btn11)

    # Answer
    rentflat1 = bot.send_message(chat_id=message.chat.id, text='Выберите Район квартиры', reply_markup=keyboard)

    def message_reply(message: Message):

        district = None

        # Не нужный код
        if message.text == "Ачапняк":
            # global district
            district = "Ачапняк"
        if message.text == "Арабкир":
            # global district
            district = "Арабкир"
        if message.text == "Аван":
            # global district
            district = "Аван"
        if message.text == "Давташен":
            # global district
            district = "Давташен"
        if message.text == "Эребуни":
            # global district
            district = "Эребуни"
        if message.text == "Канакер-Зейтун":
            # global district
            district = "Канакер-Зейтун"
        if message.text == "Кентрон":
            # global district
            district = "Кентрон"
        if message.text == "Малатия-Себастия":
            # global district
            district = "Малатия-Себастия"
        if message.text == "Норк-Мараш":
            # global district
            district = "Норк-Мараш"
        if message.text == "Нор-Норк":
            # global district
            district = "Нор-Норк"
        if message.text == "Нубарашен":
            # global district
            district = "Нубарашен"
        if message.text == "Сингавит":
            # global district
            district = "Сингавит"

        rentflat2 = bot.send_message(message.chat.id, text=f"Выбран район: {district}. Укажите описание помещения:",
                                     reply_markup=ReplyKeyboardRemove())

        def write_table(district: str):
            def wrapper(message: Message) -> None:
                description = message.text
                contact = message.from_user.username
                fn = "xlsx/rentflat.xlsx"
                wb = load_workbook(fn)
                ws = wb.active
                ws.append([district, description, contact])
                wb.save(fn)
                wb.close()

                # bot.send_message(message.chat.id, text=f"""Запись о сдаче квартиры с параметрами:
                # Район: {district}
                # Описание: {description}
                # Контакты: {contact}
                # Успешно создана!""",reply_markup=ReplyKeyboardRemove())
            return wrapper

        # Regist next context to answer
        bot.register_next_step_handler(rentflat2, write_table(district))

        return district

    # Register next context to answer
    bot.register_next_step_handler(rentflat1, message_reply)
