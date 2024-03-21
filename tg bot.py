import telebot
from telebot import types
import random
import wikipedia



wikipedia.set_lang('ru')
token ="7161973176:AAG4o9a0igmmdCvArFSMT0K5aW7lK7Fy8kM"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def send_welcome(massage):
    welcome_text = """
    Привет! Я телеграмм бот Raphael , нацеленный рассказать о полуострове Крым.
    """
    print(massage)


    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("/Крым")

    keyboard.add(button1)

    bot.send_message(massage.chat.id, welcome_text, reply_markup= keyboard)


@bot.message_handler(commands=['Крым'])
def function(message):
    text = "Крым это полуостров в Восточной Европе, на северном побережье Черного моря, почти полностью окруженный Черным и меньшим по размеру Азовским морями,. Перекопский перешеек соединяет полуостров с Херсонской областью . На востоке Крымский мост, построенный в 2018 году, пересекает Керченский пролив, соединяя полуостров с Краснодарским краем в России. Арабатская коса, расположенна."
    photo = open('D:/tg bot/img/karta1.jpg', 'rb')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    inbutton1 = telebot.types.InlineKeyboardButton("История воссоединения 🏛️", callback_data="history")
    inbutton2 = telebot.types.InlineKeyboardButton("Достопримечательности 🏰", callback_data="additional_note1")
    inbutton3 = telebot.types.InlineKeyboardButton("Карта 🗺️", callback_data="map")

    markup.add(inbutton1, inbutton2, inbutton3)
    bot.send_photo(message.chat.id, photo=photo)
    bot.send_message(message.chat.id, text, reply_markup= markup)


@bot.callback_query_handler(func=lambda callback: callback)
def callback(callback):
    if callback:
        if callback.data == 'history':
            photo = open('img/refer1.jpg', 'rb')
            history = "События 2013-2014 гг. в Киеве не только породили политический кризис на Украине, но и подтолкнули жителей Крыма и Севастополя к активизации по возвращению полуострова в состав России.16 марта 2014 года в Крыму состоялся референдум, в котором, по официальным данным, приняло участие около 82 % избирателей, из них 96 % проголосовали за вхождение в Российскую Федерацию. 17 марта 2014 года Республика Крым и Севастополь обратились с просьбой о присоединении к России. 18 марта 2014 года подписан межгосударственный Договор между Российской Федерацией, Республикой Крым и Севастополем о принятии их в состав Российской Федерации."
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            inbutton2 = telebot.types.InlineKeyboardButton( "Новости 2014 года ",callback_data="video")
            inbutton1 = telebot.types.InlineKeyboardButton( "Годовщина воссоединения ",callback_data="video10")

            markup.add(inbutton1, inbutton2, )
            bot.send_photo(callback.message.chat.id, photo= photo)
            bot.send_message(callback.message.chat.id, history, reply_markup=markup )
        elif callback.data == 'additional_note1':
            additional_note = "Полный список достапримечательностей крыма очень велик . На по-ве Крым более 100 живописных мест отличающееся своей историей и нынешним состоянием. Наболее известными местами являются - Ласточкино гнездо, Ханский дворец, Дворец харакс, Массандровский дворец, Водопад Учан-су  "
            photo = open('img/item1.jpg', 'rb')
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            inbutton1 = telebot.types.InlineKeyboardButton("Ласточкино гнездо", callback_data='1')
            inbutton2 = telebot.types.InlineKeyboardButton("Ханский дворец", callback_data='2')
            inbutton3 = telebot.types.InlineKeyboardButton("Дворец харакс", callback_data='3')
            inbutton4 = telebot.types.InlineKeyboardButton("Массандровский дворец ", callback_data='4')
            inbutton5 = telebot.types.InlineKeyboardButton("Водопад Учан-су ", callback_data='5')

            markup.add(inbutton1, inbutton2, inbutton3, inbutton4, inbutton5)
            bot.send_photo(callback.message.chat.id, photo= photo)
            bot.send_message(callback.message.chat.id, additional_note, reply_markup=markup)
        elif callback.data == 'map':
            map = " https://crimea-map.com/#m=11/44.90501/34.20387&l=O/Wh Это интерактивная карта Крыма , со все возможными видами карт"
            bot.send_message(callback.message.chat.id, map)
        if callback.data == '1':
            photo = open('img/ласточкино гнездо.jpg', 'rb')
            Lastoch = "«Ла́сточкино гнездо́»  — псевдоготический замок, расположенный на отвесной 40-метровой скале мыса Ай-Тодор в посёлке Гаспра Ялтинского городского округа Крыма. Нынешний облик принял в 1912 году. Отстроен был для богатой дворянской династии. После революции 1917 г. в разные годы в нём размещались склады, рестораны, читальные залы. Сегодня – архитектурно-выставочный комплекс, включающий несколько ярусов смотровых площадок, постоянную экспозицию об истории замка и выставочные площади"
            bot.send_photo(callback.message.chat.id, photo=photo)
            bot.send_message(callback.message.chat.id, Lastoch)
        elif callback.data == '2':
            han = wikipedia.page('Ханский дворец в крыму')
            han_link = han.summary
            photo = open('img/han.jpg', 'rb')
            bot.send_photo(callback.message.chat.id, photo=photo)
            bot.send_message(callback.message.chat.id, han_link )
        elif callback.data == '3':
            photo= open('img/har.jpg', 'rb')
            haracks = wikipedia.page('Дворец Харакс в Крыму')
            haracks_link = haracks.summary

            bot.send_photo(callback.message.chat.id, photo=photo)
            bot.send_message(callback.message.chat.id, haracks_link)
        elif callback.data == '4':
            photo = open('img/mas.jpg', 'rb')
            mas = wikipedia.page('Массандровский дворец в Крыму')
            mas_link = mas.summary
            bot.send_photo(callback.message.chat.id, photo=photo)
            bot.send_message(callback.message.chat.id, mas_link)
        elif callback.data == '5':
            photo = open('img/waterfall.jpg', 'rb')
            waterfall = wikipedia.page('Водопад Учан-су в Крыму')
            waterfall_link = waterfall.summary
            bot.send_photo(callback.message.chat.id, photo=photo)
            bot.send_message(callback.message.chat.id, waterfall_link)
        elif callback.data =='video':
            video = "https://www.1tv.ru/n/46505"
            bot.send_message(callback.message.chat.id, video)
        elif callback.data =="video10":
            video10 = 'https://www.1tv.ru/n/472816'
            bot.send_message(callback.message.chat.id, video10)


bot.polling()
