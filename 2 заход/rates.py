from bs4 import BeautifulSoup
from datetime import date
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}
BTC_USD = 'https://www.google.com/search?q=btc+usd&sxsrf=APq-WBvnzPGaB-S-3fEPLy4wdvL3RHlhpw%3A1651082053166&ei=RYNpYtnqCfD2qwGul724Bw&ved=0ahUKEwiZoZj657T3AhVw-yoKHa5LD3cQ4dUDCA0&uact=5&oq=btc+usd&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIECAAQQzIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQQzILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoHCAAQgAQQCjoGCAAQFhAeOhAILhCABBCHAhDHARDRAxAUOgoIABCABBCHAhAUOgcIABCxAxBDOggIABCABBCxA0oECEEYAEoECEYYAFDT7ANY2IEEYNGCBGgEcAF4AIABZogB8AWSAQM2LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'
BTC_AMD = 'https://www.google.com/search?q=btc+amd&sxsrf=APq-WBtFpcd99r_UjuX9R6s9SNMsyYtDeg%3A1651082044307&ei=PINpYtS3Eu7yqwH6qYP4Cw&ved=0ahUKEwjUxfv157T3AhVu-SoKHfrUAL8Q4dUDCA0&uact=5&oq=btc+фьв&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEcyBAgAEEdKBAhBGABKBAhGGABQAFgAYKgKaABwAngAgAEAiAEAkgEAmAEAyAEFwAEB&sclient=gws-wiz'
BTC_RUB = 'https://www.google.com/search?q=btc+rub&sxsrf=APq-WBut5HbkXibcZL5npAkooHT8gRUoRg%3A1651082286282&ei=LoRpYr_zEKGrrgT7moPQCg&ved=0ahUKEwi_wqzp6LT3AhWhlYsKHXvNAKoQ4dUDCA0&uact=5&oq=btc+rub&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxCwAxAnOgcIABBHELADOhIILhDHARDRAxDIAxCwAxBDGAE6BAgjECc6CwgAEIAEELEDEIMBOggIABCABBCxAzoECAAQQzoQCAAQgAQQhwIQsQMQgwEQFDoHCAAQgAQQCkoECEEYAEoECEYYAFCWBFizDGD0D2gBcAF4AIABZ4gBrQSSAQM0LjKYAQCgAQHIAQvAAQHaAQQIARgI&sclient=gws-wiz'
pageBU = requests.get(BTC_USD, headers=headers)
pageBA = requests.get(BTC_AMD, headers=headers)
pageBR = requests.get(BTC_RUB, headers=headers)
soupBU = BeautifulSoup(pageBU.content, 'html.parser')
soupBA = BeautifulSoup(pageBA.content, 'html.parser')
soupBR = BeautifulSoup(pageBR.content, 'html.parser')
resBU = soupBU.findAll("span", {"class": "pclqee"})
resBA = soupBA.findAll("span", {"class": "pclqee"})
resBR = soupBR.findAll("span", {"class": "pclqee"})

site = 'http://rate.am/ru/armenian-dram-exchange-rates/banks/non-cash'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}
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
current_date = date.today()
amdrublink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/amd/rub.json")
rubamdlink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/rub/amd.json")
usdrublink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/usd/rub.json")
usdamdlink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/usd/amd.json")
eurrublink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/eur/rub.json")
euramdlink = requests.get(f"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/{current_date}/currencies/eur/amd.json")
ardata = amdrublink.json()
radata = rubamdlink.json()
urdata = usdrublink.json()
uadata = usdamdlink.json()
erdata = eurrublink.json()
eadata = euramdlink.json()
amdrub = ardata['rub']
rubamd = radata['amd']
usdrub = urdata['rub']
usdamd = uadata['amd']
eurrub = erdata['rub']
euramd = eadata['amd']
ratestext = f"""
	**Кросс-курс**\n1 ֏ = `{'%.2f'%amdrub}` ₽
	1₽ = `{'%.2f'%rubamd}` ֏
	1$ = `{'%.2f'%usdrub}` ₽/`{'%.2f'%usdamd}` ֏
	1€ = `{'%.2f'%eurrub}` ₽/`{'%.2f'%euramd}` ֏
	**Топ 5 банков с самым выгодным курсом обмена**:
	
	🇺🇸 Доллар 🇺🇸:
	[Меллат Банк](https://www.google.com/search?q=Меллат+Банк) > `{Mellat[5].text}` ֏ 
	[Арарат Банк](https://www.google.com/search?q=Арарат+Банк) > `{Ararat[5].text}` ֏
	[ВТБ Армения](https://www.google.com/search?q=ВТБ+Армения) > `{VTBarmenia[5].text}` ֏
	[Эйч-Эс-Би-Си Банк Армения](https://www.google.com/search?q=Эйч-Эс-Би-Си+Банк+Армения) > `{HSBCbank[5].text}` ֏
	[Конверс Банк](https://www.google.com/search?q=Конверс+Банк) > `{ConverseBank[5].text}` ֏
	
	🇪🇺 Евро 🇪🇺:
	[Армсвисбанк](https://www.google.com/search?q=Армсвисбанк) > `{Armsvisbank[7].text}` ֏ 
	[Меллат Банк](https://www.google.com/search?q=Меллат+Банк) > `{Mellat[7].text}` ֏
	[Юнибанк/Армения](https://www.google.com/search?q=Юнибанк+Армения) > `{Unibank[7].text}` ֏
	[Библос Банк Армения](https://www.google.com/search?q=Библос+Банк+Армения) > `{Biblos[7].text}` ֏
	[Акба банк](https://www.google.com/search?q=Акба+Банк) > `{AkbaBank[7].text}` ֏

	🇷🇺 Рубль 🇷🇺:
	[Меллат Банк](https://www.google.com/search?q=Меллат+Банк) >`{Mellat[9].text}` ֏
	[Библос Банк Армения](https://www.google.com/search?q=Библос+Банк+Армения) > `{Biblos[9].text}` ֏
	[ВТБ Армения](https://www.google.com/search?q=ВТБ+Армения) > `{VTBarmenia[9].text}` ֏
	[Инекобанк](https://www.google.com/search?q=Инекобанк) > `{inecobank[9].text}` ֏ 
	[Эйч-Эс-Би-Си Банк Армения](https://www.google.com/search?q=Эйч-Эс-Би-Си+Банк+Армения) > `{HSBCbank[9].text}` ֏
	

	[Bitcoin](https://www.google.com/search?q=bitcoin):
	🇺🇸:`{resBU[0].text}`$ 🇦🇲:`{resBA[0].text}` ֏ 🇷🇺:`{resBR[0].text}` ₽
	"""