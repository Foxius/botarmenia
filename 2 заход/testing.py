from pyrogram import Client
from pyrogram import filters
from config import *
import colorama
from colorama import Fore
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
@bot.on_message(filters.media_group)
def photo(bot, msg):
    req = bot.get_media_group(msg.chat.id, msg.id)
    lst=[]
    lst2= []
    reqdata = req.json()
    for i in req:
        if not i.photo.file_id[:-9] in lst2:
            lst2.append(i.photo.file_id[:-9])
            lst.append(i.photo.file_id)
    photos = [pyrogram.types.InputMediaPhoto(file) for file in lst]
    print(lst)
    bot.send_media_group(message.chat.id, photos)

bot.run()