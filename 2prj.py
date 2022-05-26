

	***Поиск квартиры***
	/searchflat - Оставьте заявку на поиск съёмной квартиры в Ереване
	/rentflallist - Список всех доступных для аренды квартир

	***Сдача квартиры***
	/rentflat - Разместить объявление о сдачи квартиры в Ереване
	/searchflatlist - Список пользователей ищущих квартиру

	***Покупка/Продажа товаров***
	/buy - разместить объявление о покупке/поиске товара
	/selllist - Лист товаров доступных для покупки
	/sell - Разместить объявление о продаже товара
	/buylist - лист пользователей, готовых купить определенный товар

	***Поиск вакансии/резюме***
	/work - разместить объявление о поиске работы
	/worker - разместить объявление о поиске сотрудника
	/worklist - список доступных резюме
	/workerlist - список доступных вакансий

	***Услуги в Ереване***
	/servicesearch - список всех доступных услуг в Ереване
	/servicesuggestion - предложение услуг в Ереван


	class IsPrivate(telebot.custom_filters.SimpleCustomFilter):
    key='is_private'
    @staticmethod
    def check(message: telebot.types.Message):
        return message.chat.type == "private"

bot.add_custom_filter(IsPrivate())

@bot.message_handler(commands=['searchflat'], is_private=True)
def rentflat(message: types.Message):
	keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	btn = types.KeyboardButton("Ачапняк")
	keyboard.add(btn)
	btn1 = types.KeyboardButton("Арабкир")
	keyboard.add(btn1)
	btn2 = types.KeyboardButton("Аван")
	keyboard.add(btn2)
	btn3 = types.KeyboardButton("Давташен")
	keyboard.add(btn3)	
	btn4 = types.KeyboardButton("Эребуни")
	keyboard.add(btn4)	
	btn5 = types.KeyboardButton("Канакер-Зейтун")
	keyboard.add(btn5)	
	btn6 = types.KeyboardButton("Кентрон")
	keyboard.add(btn6)	
	btn7 = types.KeyboardButton("Малатия-Себастия")
	keyboard.add(btn7)	
	btn8 = types.KeyboardButton("Норк-Мараш")
	keyboard.add(btn8)	
	btn9 = types.KeyboardButton("Нор-Норк")
	keyboard.add(btn9)	
	btn10 = types.KeyboardButton("Нубарашен")
	keyboard.add(btn10)	
	btn11 = types.KeyboardButton("Шенгавит")
	keyboard.add(btn11)
	searchflat1 = bot.send_message(message.chat.id, text='Выберите Район поиска квартиры',reply_markup=keyboard)
	bot.register_next_step_handler(searchflat1,chekingdis)
def chekingdis(message):
	if message.text=="Ачапняк":
		district = "Ачапняк"
	if message.text=="Арабкир":
		district = "Арабкир"
	if message.text=="Аван":
		district = "Аван"	
	if message.text=="Давташен":
		district = "Давташен"
	if message.text=="Эребуни":
		district = "Эребуни"			
	if message.text=="Канакер-Зейтун":
		district = "Канакер-Зейтун"
	if message.text=="Кентрон":
		district = "Кентрон"
	if message.text=="Малатия-Себастия":
		district = "Малатия-Себастия"
	if message.text=="Норк-Мараш":		
		district = "Норк-Мараш"
	if message.text=="Нор-Норк":		
		district = "Нор-Норк"
	if message.text=="Нубарашен":
		district = "Нубарашен"
	if message.text=="Сингавит":
		district = "Сингавит"
	file = open("temptxt/searchflat.txt", "w")
	file.write(district)
	searchflat2 = bot.send_message(message.chat.id, text=f"""Выбран район: {district} """,reply_markup=types.ReplyKeyboardRemove())
	searchflat3 = bot.send_message(message.chat.id,'Укажите описание Поиска:',reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(searchflat3,writetablesearch)
def writetablesearch(message):
	file = open("temptxt/searchflat.txt", "r")
	district = file.readline()
	description = message.text
	contact = '@'+ message.from_user.username
	# fn = "xlsx/basadate.xlsx"
	# wb = load_workbook(fn)
	# ws = wb['searchflat']
	# ws.append([district, description, contact])
	# wb.save(fn)
	# wb.close()
	txt = f"""Запись о поиске квартиры с параметрами:
	Район: {district}
	Описание: {description}
	Контакты: {contact}
	Успешно отправлена на модерацию!"""
	txtmod = f"""Новая запись о поиске квартиры с параметрами:
	Район: {district}
	Описание: {description}
	Контакты: {contact}
	Просьба модераторов проверить и занести в общий реестр"""
	bot.send_message(message.chat.id, text=txt ,reply_markup=types.ReplyKeyboardRemove())
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)

@bot.message_handler(commands=['rentflat'], is_private=True)
def rentflat(message: types.Message):
	keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	btn = types.KeyboardButton("Ачапняк")
	keyboard.add(btn)
	btn1 = types.KeyboardButton("Арабкир")
	keyboard.add(btn1)
	btn2 = types.KeyboardButton("Аван")
	keyboard.add(btn2)
	btn3 = types.KeyboardButton("Давташен")
	keyboard.add(btn3)	
	btn4 = types.KeyboardButton("Эребуни")
	keyboard.add(btn4)	
	btn5 = types.KeyboardButton("Канакер-Зейтун")
	keyboard.add(btn5)	
	btn6 = types.KeyboardButton("Кентрон")
	keyboard.add(btn6)	
	btn7 = types.KeyboardButton("Малатия-Себастия")
	keyboard.add(btn7)	
	btn8 = types.KeyboardButton("Норк-Мараш")
	keyboard.add(btn8)	
	btn9 = types.KeyboardButton("Нор-Норк")
	keyboard.add(btn9)	
	btn10 = types.KeyboardButton("Нубарашен")
	keyboard.add(btn10)	
	btn11 = types.KeyboardButton("Шенгавит")
	keyboard.add(btn11)
	rentflat1 = bot.send_message(message.chat.id, text='Выберите Район квартиры',reply_markup=keyboard)
	bot.register_next_step_handler(rentflat1,message_reply)
def message_reply(message):
	if message.text=="Ачапняк":		
		district = "Ачапняк"
	if message.text=="Арабкир":
		district = "Арабкир"
	if message.text=="Аван":		
		district = "Аван"	
	if message.text=="Давташен":	
		district = "Давташен"
	if message.text=="Эребуни":		
		district = "Эребуни"			
	if message.text=="Канакер-Зейтун":
		district = "Канакер-Зейтун"
	if message.text=="Кентрон":		
		district = "Кентрон"
	if message.text=="Малатия-Себастия":
		district = "Малатия-Себастия"
	if message.text=="Норк-Мараш":
		district = "Норк-Мараш"
	if message.text=="Нор-Норк":
		district = "Нор-Норк"
	if message.text=="Нубарашен":
		district = "Нубарашен"
	if message.text=="Сингавит":
		district = "Сингавит"
	file = open("temptxt/rentflat.txt", "w")
	file.write(district)
	rentflat2 = bot.send_message(message.chat.id, text=f"""Выбран район: {district} """,reply_markup=types.ReplyKeyboardRemove())
	rentflat3 = bot.send_message(message.chat.id,'Отправьте одну фотографию помещения:',reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(rentflat3,photorentflat)
def photorentflat(message):
	file_path = bot.get_file(message.photo[0].file_id).file_path
	file = bot.download_file(file_path)
	with open("rentflatphoto.png", "wb") as code:
		code.write(file)
	rentflat4 = bot.send_message(message.chat.id,'Укажите описание помещения:',reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(rentflat4,writetable)
def writetable(message):
	file = open("temptxt/rentflat.txt", "r", encoding ='cp1251')
	district = file.readline()
	description = message.text
	contact = message.from_user.username
	rentflattext = (f"""Запись о сдаче квартиры с параметрами:
	Район: {district}
	Описание: {description}
	Контакты: @{contact}
	Успешно создана!""")
	photo = open("rentflatphoto.png")
	bot.send_photo(message.chat.id, photo, caption = rentflattext)
	channel_id = -1001680279204
	bot.send_photo(channel_id, photo, caption = rentflattext)
@bot.message_handler(commands=['buy'], is_private=True)
def buystart(message):
	buystart = bot.send_message(message.chat.id, text="Введите название интересующего Вас товара")
	bot.register_next_step_handler(buystart, buy)
def buy(message):
	titlebuy = message.text
	file = open("temptxt/buy.txt", "w")
	file.write(message.text)
	buy = bot.send_message(message.chat.id, text="Отлично, теперь введите описание товара")
	bot.register_next_step_handler(buy, buywritetable)
def buywritetable(message):
	descbuy = message.text
	file = open("temptxt/buy.txt", "r")
	titlebuy = file.readline()
	contact = message.from_user.username
	workbook = load_workbook("xlsx/basadate.xlsx")
	sheet = workbook['buy']
	sheet.append([titlebuy, descbuy, contact])
	workbook.save("xlsx/basadate.xlsx")
	workbook.close()
	txtmod = f"""Новая запись о поиске товара с параметрами:
	Название: {titlebuy}
	Описание: {descbuy}
	Контакты: {contact}
	Просьба модераторов проверить и занести в общий реестр"""
	bot.send_message(message.chat.id, text=f"""Запись о поиске товара с параметрами:
	Название: {titlebuy}
	Описание: {descbuy}
	Контакты: {contact}
	Успешно отправлена на модерацию!""",reply_markup=types.ReplyKeyboardRemove())
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)

@bot.message_handler(commands=['sell'], is_private=True)
def sellstart(message):
	sellstart = bot.send_message(message.chat.id, text="Введите название Вашего товара")
	bot.register_next_step_handler(sellstart, sell)
def sell(message):
	titlesell = message.text
	file = open("temptxt/sell.txt", "w")
	file.write(message.text)
	sell = bot.send_message(message.chat.id, text="Отлично, теперь введите стоимость Вашего товара")
	bot.register_next_step_handler(sell, count)
def count(message):
	count = message.text
	file = open("temptxt/sell1.txt", "w")
	file.write(message.text)
	count = bot.send_message(message.chat.id, text="Замечательно, теперь введите описание Вашего товара")
	bot.register_next_step_handler(count, sellwritetable)
def sellwritetable(message):
	descsell = message.text
	file1 = open("temptxt/sell.txt", "r")
	titlesell = file1.readline()
	file = open("temptxt/sell1.txt", "r")
	count = file.readline()
	contact = message.from_user.username
	# workbook = load_workbook("xlsx/basadate.xlsx")
	# sheet = workbook['sell']
	# sheet.append([titlesell, count, descsell, contact])
	# workbook.save("xlsx/basadate.xlsx")
	# workbook.close()
	txtmod = f"""Новое Объявление о продаже с параметрами:
		Название: {titlesell}
		Стоимость: {count}
		Описание: {descsell}
		Контакты: @{contact}
		Просьба модераторов проверить и занести в общий реестр
		"""
	bot.send_message(message.chat.id, text=f"""Объявление о продаже с параметрами:
		Название: {titlesell}
		Стоимость: {count}
		Описание: {descsell}
		Контакты: @{contact}
		Успешно отправлено на модерацию!
		""",reply_markup=types.ReplyKeyboardRemove())
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)
@bot.message_handler(commands=['work'], is_private=True)
def workstart(message):
	workstart = bot.send_message(message.chat.id, text="Введите название Вашего резюме")
	bot.register_next_step_handler(workstart, work)
def work(message):
	titlework = message.text
	file = open("temptxt/work.txt", "w")
	file.write(message.text)
	work = bot.send_message(message.chat.id, text="Прекрасно, теперь расскажите о себе поподробнее")
	bot.register_next_step_handler(work, workwritetable)
def workwritetable(message):
	descwork = message.text
	file = open("temptxt/work.txt", "r")
	titlework = file.readline()
	contact = message.from_user.username
	# workbook = load_workbook("xlsx/basadate.xlsx")
	# sheet = workbook['work']
	# sheet.append([titlework, descwork, contact])
	# workbook.save("xlsx/basadate.xlsx")
	# workbook.close()
	txtmod = f"""Новое резюме с параметрами:
		Название: {titlework}
		Описание: {descwork}
		Контакты: @{contact}
		Просьба модераторов проверить и занести в общий реестр
		"""
	bot.send_message(message.chat.id, text=f"""Новое резюме с параметрами:
		Название: {titlework}
		Описание: {descwork}
		Контакты: @{contact}
		Успешно отправлено на модерацию!
		""",reply_markup=types.ReplyKeyboardRemove())
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)
@bot.message_handler(commands=['worker'], is_private=True)
def workerstart(message):
	workerstart = bot.send_message(message.chat.id, text="Введите название вашей вакансии")
	bot.register_next_step_handler(workerstart, worker)
def worker(message):
	titlework = message.text
	file = open("temptxt/worker.txt", "w")
	file.write(message.text)
	worker = bot.send_message(message.chat.id, text="Отлично, теперь введите заработную плату")
	bot.register_next_step_handler(worker, countworker)
def countworker(message):
	countworker = message.text
	file = open("temptxt/worker1.txt", "w")
	file.write(message.text)
	countworker = bot.send_message(message.chat.id, text="Замечательно, теперь введите описание Вашей вакансии")
	bot.register_next_step_handler(countworker, workerwritetable)
def workerwritetable(message):
	descworker = message.text
	file1 = open("temptxt/worker.txt", "r")
	titleworker = file1.readline()
	file = open("temptxt/worker1.txt", "r")
	countworker = file.readline()
	contact = message.from_user.username
	# workbook = load_workbook("xlsx/basadate.xlsx")
	# sheet = workbook['worker']
	# sheet.append([titleworker, countworker, descworker, contact])
	# workbook.save("xlsx/basadate.xlsx")	
	workbook.close()
	txtmod = f"""Новое Объявление о новой вакансии с параметрами:
		Название: {titleworker}
		Стоимость: {countworker}
		Описание: {descworker}
		Контакты: @{contact}
		Просьба модераторов проверить и занести в общий реестр!
		"""
	bot.send_message(message.chat.id, text=f"""Объявление о новой вакансии с параметрами:
		Название: {titleworker}
		Стоимость: {countworker}
		Описание: {descworker}
		Контакты: @{contact}
		Успешно отправлено на модерацию!
		""",reply_markup=types.ReplyKeyboardRemove())
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)
@bot.message_handler(commands=['servicesuggestion'], is_private=True)
def servicesuggestionstart(message):
	servicesuggestionstart = bot.send_message(message.chat.id, text="Введите название Вашей услуги")
	bot.register_next_step_handler(servicesuggestionstart, servicesuggestion)
def servicesuggestion(message):
	titleservicesuggestion = message.text
	file = open("temptxt/servicesuggestion.txt", "w")
	file.write(message.text)
	servicesuggestion = bot.send_message(message.chat.id, text="Прекрасно, теперь расскажите о услуге поподробнее")
	bot.register_next_step_handler(servicesuggestion, servicesuggestionwritetable)
def servicesuggestionwritetable(message):
	descservicesuggestion = message.text
	file = open("temptxt/servicesuggestion.txt", "r")
	titleservicesuggestion = file.readline()
	contact = message.from_user.username
	# workbook = load_workbook("xlsx/basadate.xlsx")
	# sheet = workbook['work']
	# sheet.append([titleservicesuggestion, descservicesuggestion, contact])
	# workbook.save("xlsx/basadate.xlsx")
	# workbook.close()
	bot.send_message(message.chat.id, text=f"""Новая услуга с параметрами:
		Название: {titleservicesuggestion}
		Описание: {descservicesuggestion}
		Контакты: @{contact}
		Успешно отправлено на модерацию!
		""",reply_markup=types.ReplyKeyboardRemove())
	txtmod = f"""Новая услуга с параметрами:
		Название: {titleservicesuggestion}
		Описание: {descservicesuggestion}
		Контакты: @{contact}
		Просьба модераторов проверить и занести в общий реестр!
		"""
	channel_id = -1001680279204
	bot.send_message(channel_id, text=txtmod)
#модуль листинга
# @bot.message_handler(commands=['rentflatlist'], is_private=True)
# def rentflatlist(message):
# 	book = load_workbook(filename = 'xlsx/basadate.xlsx')
# 	sheet = book["rentflat"]
# 	for row in range(1,sheet.max_row):
# 			district = sheet[row][0].value
# 			description = sheet[row][1].value
# 			contact = sheet[row][2].value
# 			bot.send_message(message.chat.id, text=f"""<u>Сдаю квартиру:</u>
# 				<b>Район квартиры</b>: <i>{district}</i>
# 				<b>Описание квартиры</b>: <i>{description}</i>
# 				<b>Контакты телеграм для связи</b>: <code>{contact}</code>
# 				""", parse_mode = 'HTML')
