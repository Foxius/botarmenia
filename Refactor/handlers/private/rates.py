# Модуль для обработки URL
import requests
from ...run import bot
# Модуль для работы с HTML
from bs4 import BeautifulSoup
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(commands=['rates'])
def rates(message):
    AMD_RUB = 'https://www.google.com/search?q=dram+rubli&sxsrf=APq-WBsaGvvcDu6LhUgt1q7bIjaVSK3tyA%3A1650901995344&ei=68NmYv_UFPClrgTXxLHgDQ&oq=dram+&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgoILhDHARCjAhAnOgQIIxAnOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6CAgAEIAEELEDOgsIABCABBAKEAEQKjoJCAAQgAQQChABOgkILhCABBAKEAE6CggAELEDEIMBEEM6BAgAEEM6BAguEEM6BwgjEOoCECc6DgguEIAEELEDEMcBEKMCOggILhCABBDUAjoGCCMQJxATOgcIABCxAxBDOgcILhCxAxBDOgoILhCxAxCDARBDSgQIQRgASgQIRhgAUABYrxVg1iBoBHABeACAAXCIAfoGkgEDNC41mAEAoAEBsAEKwAEB&sclient=gws-wiz'
    RUB_AMD = 'https://www.google.com/search?q=rubli+dram&sxsrf=APq-WBu4-O_4-pQh80GnDlqjka7ofdQ73Q%3A1650903989881&source=hp&ei=tctmYuSkM7GOxc8Pp_umoAQ&iflsig=AHkkrS4AAAAAYmbZxYt8d79ipaJlGGU63bOsA18ZbEMv&oq=rubil+dra&gs_lcp=Cgdnd3Mtd2l6EAMYADIJCAAQDRBGEIICMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANOgQIIxAnOg4ILhCABBCxAxDHARCjAjoICAAQgAQQsQM6BQgAEIAEOggILhCABBDUAjoGCCMQJxATOgsIABCABBCxAxCDAToRCC4QgAQQsQMQxwEQ0QMQ1AI6DgguEIAEELEDEMcBENEDOgsILhCABBCxAxCDAToICC4QgAQQsQM6BQguEIAEOgoILhCABBDUAhAKOgcIIxDqAhAnOhEILhCABBCxAxCDARDHARDRAzoLCC4QsQMQxwEQowI6CAgAELEDEIMBOhAIABCABBCHAhCxAxCDARAUOhUIABCABBCHAhCxAxCDARAUEEYQggI6CwguEIAEEMcBENEDOgsILhCABBCxAxDUAjoRCC4QgAQQsQMQgwEQxwEQrwE6FAguEIAEELEDEIMBEMcBENEDENQCOgcIABCABBAKOgoIABCxAxCDARAKOgcIABCxAxAKOgQIABAKOgYIABANEAo6CAgAEA0QChAeOgYIABAWEB46CAgAEBYQChAeOgoIABANEAUQChAeUABYkz1gi0doCXAAeACAAZoBiAHvC5IBAzcuN5gBAKABAbABCg&sclient=gws-wiz'
    USD_RUB = 'https://www.google.com/search?q=usd+rub&sxsrf=APq-WBtHT3JXpjCC6U3ao5O63aTM5WzAOg%3A1650904244105&ei=tMxmYqGSBuOqrgSyyovYBA&ved=0ahUKEwihvJzI0a_3AhVjlYsKHTLlAksQ4dUDCA0&uact=5&oq=usd+rub&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIICAAQgAQQsQMyCggAELEDEIMBEEMyBQgAEIAEMgUIABCABDIKCAAQgAQQhwIQFDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoECCMQJzoECAAQQzoMCCMQsQIQJxBGEIICOgcIABCxAxAKOgQIABAKSgQIQRgASgQIRhgAUPgCWOwJYIgMaAJwAXgAgAF0iAGHA5IBAzMuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'
    USD_AMD = 'https://www.google.com/search?q=usd+dram&sxsrf=APq-WBtzKeJYiT7Yc6GWXUCtHNnA8Qq9Og%3A1650904002133&ei=wstmYr7lB4eXrwSqtK6YAg&ved=0ahUKEwi-zuvU0K_3AhWHy4sKHSqaCyMQ4dUDCA0&uact=5&oq=usd+dram&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgUIABCABDoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQzoECAAQAjoICAAQBxAKEB5KBAhBGABKBAhGGABQowxYzw9g-BBoAnABeACAAd0BiAGhA5IBBTEuMS4xmAEAoAEByAEKwAEB&sclient=gws-wiz'
    EUR_RUB = 'https://www.google.com/search?q=eur+rub&sxsrf=APq-WBuzQkvXlhRu_zaEKjIY7s2hrA6REg%3A1650904246802&ei=tsxmYv_NMImdrgSi1YH4BQ&ved=0ahUKEwj_gMHJ0a_3AhWJjosKHaJqAF8Q4dUDCA0&uact=5&oq=eur+rub&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgQIABBDMgUIABCABDIFCAAQgAQ6BggAEAcQHkoECEEYAEoECEYYAFAAWMsDYMwGaABwAXgBgAHPAYgB-gOSAQUxLjAuMpgBAKABAcABAQ&sclient=gws-wiz'
    EUR_AMD = 'https://www.google.com/search?q=eur+amd&sxsrf=APq-WBs7Vj-yKcpzTdsgejErA--SRJGESw%3A1650904266885&ei=ysxmYpXYNYWbrgTj-beYDw&ved=0ahUKEwiV5YrT0a_3AhWFjYsKHeP8DfMQ4dUDCA0&uact=5&oq=eur+amd&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQFhAKEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoECAAQQzoKCAAQgAQQhwIQFEoECEEYAEoECEYYAFDCA1ifBWCwBmgBcAF4AIABc4gBvQKSAQMxLjKYAQCgAQHIAQrAAQE&sclient=gws-wiz'

    BTC_USD = 'https://www.google.com/search?q=btc+usd&sxsrf=APq-WBvnzPGaB-S-3fEPLy4wdvL3RHlhpw%3A1651082053166&ei=RYNpYtnqCfD2qwGul724Bw&ved=0ahUKEwiZoZj657T3AhVw-yoKHa5LD3cQ4dUDCA0&uact=5&oq=btc+usd&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIECAAQQzIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQQzILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoHCAAQgAQQCjoGCAAQFhAeOhAILhCABBCHAhDHARDRAxAUOgoIABCABBCHAhAUOgcIABCxAxBDOggIABCABBCxA0oECEEYAEoECEYYAFDT7ANY2IEEYNGCBGgEcAF4AIABZogB8AWSAQM2LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'
    BTC_AMD = 'https://www.google.com/search?q=btc+amd&sxsrf=APq-WBtFpcd99r_UjuX9R6s9SNMsyYtDeg%3A1651082044307&ei=PINpYtS3Eu7yqwH6qYP4Cw&ved=0ahUKEwjUxfv157T3AhVu-SoKHfrUAL8Q4dUDCA0&uact=5&oq=btc+фьв&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEdKBAhBGABKBAhGGABQAFgAYKgKaABwAngAgAEAiAEAkgEAmAEAyAEFwAEB&sclient=gws-wiz'
    BTC_RUB = 'https://www.google.com/search?q=btc+rub&sxsrf=APq-WBut5HbkXibcZL5npAkooHT8gRUoRg%3A1651082286282&ei=LoRpYr_zEKGrrgT7moPQCg&ved=0ahUKEwi_wqzp6LT3AhWhlYsKHXvNAKoQ4dUDCA0&uact=5&oq=btc+rub&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxCwAxAnOgcIABBHELADOhIILhDHARDRAxDIAxCwAxBDGAE6BAgjECc6CwgAEIAEELEDEIMBOggIABCABBCxAzoECAAQQzoQCAAQgAQQhwIQsQMQgwEQFDoHCAAQgAQQCkoECEEYAEoECEYYAFCWBFizDGD0D2gBcAF4AIABZ4gBrQSSAQM0LjKYAQCgAQHIAQvAAQHaAQQIARgI&sclient=gws-wiz'
    # Заголовки для передачи вместе с URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}
    # Парсим всю страницу
    pageAR = requests.get(AMD_RUB, headers=headers)
    pageRA = requests.get(RUB_AMD, headers=headers)
    pageUR = requests.get(USD_RUB, headers=headers)
    pageUA = requests.get(USD_AMD, headers=headers)
    pageER = requests.get(EUR_RUB, headers=headers)
    pageEA = requests.get(EUR_AMD, headers=headers)

    pageBU = requests.get(BTC_USD, headers=headers)
    pageBA = requests.get(BTC_AMD, headers=headers)
    pageBR = requests.get(BTC_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soupAR = BeautifulSoup(pageAR.content, 'html.parser')
    soupRA = BeautifulSoup(pageRA.content, 'html.parser')
    soupUR = BeautifulSoup(pageUR.content, 'html.parser')
    soupUA = BeautifulSoup(pageUA.content, 'html.parser')
    soupER = BeautifulSoup(pageER.content, 'html.parser')
    soupEA = BeautifulSoup(pageEA.content, 'html.parser')

    soupBU = BeautifulSoup(pageBU.content, 'html.parser')
    soupBA = BeautifulSoup(pageBA.content, 'html.parser')
    soupBR = BeautifulSoup(pageBR.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    resAR = soupAR.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    resRA = soupRA.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    resUR = soupUR.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    resUA = soupUA.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    resER = soupER.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    resEA = soupEA.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    resBU = soupBU.findAll("span", {"class": "pclqee"})
    resBA = soupBA.findAll("span", {"class": "pclqee"})
    resBR = soupBR.findAll("span", {"class": "pclqee"})

    # Курсы с rate.am
    site = 'http://rate.am/ru/armenian-dram-exchange-rates/banks/non-cash'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}
    pars = requests.get(site, headers=headers)
    soup = BeautifulSoup(pars.content, 'html.parser')
    Mellat = soup.find("tr", {"id": "f288c3fc-f524-468c-bff7-fbd9bbc6b8d7"}).find_all("td")
    AkbaBank = soup.find("tr", {"id": "f3ffb6cf-dbb6-4d43-b49c-f6d71350d7fb"}).find_all("td")
    Ararat = soup.find("tr", {"id": "5ee70183-87fe-4799-802e-ef7f5e7323db"}).find_all("td")
    VTBarmenia = soup.find("tr", {"id": "69460818-02ec-456e-8d09-8eeff6494bce"}).find_all("td")
    Arcaxbank = soup.find("tr", {"id": "e1a68c2e-bc47-4f58-afd2-3b80a8465b14"}).find_all("td")
    HSBCbank = soup.find("tr", {"id": "332c7078-97ad-4bf7-b8ee-44d85a9c88d1"}).find_all("td")
    ConverseBank = soup.find("tr", {"id": "2119a3f1-b233-4254-a450-304a2a5bff19"}).find_all("td")
    Armsvisbank = soup.find("tr", {"id": "95b795f4-073d-4670-993d-dfb781375a94"}).find_all("td")
    Unibank = soup.find("tr", {"id": "133240fd-5910-421d-b417-5a9cedd5f5f7"}).find_all("td")
    Biblos = soup.find("tr", {"id": "ebd241ce-4a38-45a4-9bcd-c6e607079706"}).find_all("td")
    inecobank = soup.find("tr", {"id": "65351947-217c-4593-9011-941b88ee7baf"}).find_all("td")

    bot.send_message(message.chat.id, f"""
		***Кросс-курс***\n1֏ = `{resAR[0].text}`₽
		1₽ = `{resRA[0].text}`֏
		1$ = `{resUR[0].text}`₽/`{resUA[0].text}`֏
		1€ = `{resER[0].text}`₽/`{resEA[0].text}`֏
		***Топ 5 банков с самым выгодным курсом обмена***:

		🇺🇸 Доллар 🇺🇸:
		[Меллат Банк](https://www.google.com/search?q=Меллат+Банк)-->`{Mellat[5].text}`֏ 
		[Арарат Банк](https://www.google.com/search?q=Арарат+Банк)-->`{Ararat[5].text}`֏
		[ВТБ Армения](https://www.google.com/search?q=ВТБ+Армения)-->`{VTBarmenia[5].text}`֏
		[Эйч-Эс-Би-Си Банк Армения](https://www.google.com/search?q=Эйч-Эс-Би-Си+Банк+Армения)-->`{HSBCbank[5].text}`֏
		[Конверс Банк](https://www.google.com/search?q=Конверс+Банк)-->`{ConverseBank[5].text}`֏

		🇪🇺 Евро 🇪🇺:
		[Армсвисбанк](https://www.google.com/search?q=Армсвисбанк)-->`{Armsvisbank[7].text}`֏ 
		[Меллат Банк](https://www.google.com/search?q=Меллат+Банк)-->`{Mellat[7].text}`֏
		[Юнибанк/Армения](https://www.google.com/search?q=Юнибанк+Армения)-->`{Unibank[7].text}`֏
		[Библос Банк Армения](https://www.google.com/search?q=Библос+Банк+Армения)-->`{Biblos[7].text}`֏
		[Акба банк](https://www.google.com/search?q=Акба+Банк)-->`{AkbaBank[7].text}`֏

		🇷🇺 Рубль 🇷🇺:
		[Меллат Банк](https://www.google.com/search?q=Меллат+Банк)-->`{Mellat[9].text}`֏
		[Библос Банк Армения](https://www.google.com/search?q=Библос+Банк+Армения)-->`{Biblos[9].text}`֏
		[ВТБ Армения](https://www.google.com/search?q=ВТБ+Армения)-->`{VTBarmenia[9].text}`֏
		[Инекобанк](https://www.google.com/search?q=Инекобанк)-->`{inecobank[9].text}`֏ 
		[Эйч-Эс-Би-Си Банк Армения](https://www.google.com/search?q=Эйч-Эс-Би-Си+Банк+Армения)-->`{HSBCbank[9].text}`֏


		[Bitcoin](https://www.google.com/search?q=bitcoin):
		🇺🇸:`{resBU[0].text}`$ 🇦🇲:`{resBA[0].text}`֏ 🇷🇺:`{resBR[0].text}`₽
		""", parse_mode='Markdown', reply_markup=ReplyKeyboardRemove())
