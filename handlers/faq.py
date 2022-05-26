from stbot import bot
from telebot.types import Message, ReplyKeyboardRemove


@bot.message_handler(commands=['faq'])
def faq(message: Message):
    bot.send_message(message.chat.id, """
    ***Список всех полезных FAQ и материалов в одном месте:***\n
    [1) Выбор банка и открытие счета. Плюсы, минусы и особенности.](https://t.me/RelocaterInfo_am_chat/48)\n
    [2) Ограничения и особенности использования зарубежных счетов резидентов РФ. Пополнения, конвертации и другие часто задаваемые вопросы. Как не попасть на штрафы.](https://t.me/RelocaterInfo_am_chat/58)\n
    [3) 5 Правил финансовой безопасности в Армении.](https://t.me/RelocaterInfo_am_chat/9)\n
    [4) Список Банкоматов  в Ереване, с которых можно снять деньги используя РФ карту МИР.](https://t.me/RelocaterInfo_am_chat/61)\n
    [5) Про релокацию Бизнеса в РА.](https://t.me/RelocaterInfo_am_chat/47)\n
    [6) Где и как лучше менять деньги, список обменников Rate.am](https://t.me/RelocaterInfo_am_chat/7)\n
    7) Про аренду квартир - смотрите доступные варианты [на list.AM]( на List.AM (https://www.list.am/category/56?pfreq=1&n=1&price1=&price2=&crc=-1&_a5=0&_a39=0&_a11_1=&_a11_2=&_a4=0&_a37=0&_a3_1=&_a3_2=&_a38=0), позже распишем подробнее и про альтернативные варианты.\n
    [8) Мошенничество при Аренде квартир](https://t.me/RelocaterInfo_am_chat/43)\n
    9) Перевозка животных в/из Армении - TBD\n
    [10) Доставки еды в Армении.](https://t.me/RelocaterInfo_am_chat/65)\n
    [11) Как остаться более 180 дней в Армении. ВНЖ, регистрация и Временный выезд](https://t.me/RelocaterInfo_am_chat/82)\n
    [12) Получение гражданства РА](https://t.me/RelocaterInfo_am_chat/5).\n
    [13) Покупка вещей, рынки, техника, спорт и аналог авито - List.am](https://t.me/RelocaterInfo_am_chat/70)\n
    [14) Как перевести деньги на Ardshin и Inecobank с Тиньков и других банков. Рубли и валюту](https://t.me/RelocaterInfo_am_chat/342)\n
    [15) Early.one - ускоряем получение документов, не стоим в очередях в банках и других гос учреждениях. Онлайн запись](https://t.me/RelocaterInfo_am_chat/385)\n
    [16) Онлайн доставки лекарств из Аптек в Армении](https://t.me/RelocaterInfo_am_chat/1512)\n
    [17) Пункты вакцинации в Ереване (бесплатные)](https://t.me/RelocaterInfo_am_chat/2776)\n
    [18) Доставка с Озона, Авито, США и Европы в Армении](https://t.me/RelocaterInfo_am_chat/3183)
     """, parse_mode='Markdown', reply_markup=ReplyKeyboardRemove())
