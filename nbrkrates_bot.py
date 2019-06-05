''' Бот написан за 2 часа, в целях теста библиотек. 
Бот получает дату формирует запрос на сайт национального банка, 
дает ответ курсы валют на дату запроса  '''

import telebot #Библиотека для работы с телеграмом
import requests # Бибилотека для работы с http запросами
from xml.etree import ElementTree #Библиотека для построения XML 

bot = telebot.TeleBot("898590538:AAELbpXaz56-5l_ur-AjzdXLic5bEtXIhG0") # ключ авторизации телеграмм

@bot.message_handler(content_types=['text']) 

def send_echo(message):

    url = 'https://nationalbank.kz/rss/get_rates.cfm?fdate=' # строка запроса
    date = message.text # дата ввода из чата
    url = url + date + '&switch=russian' # формируем конечный запрос

    r = requests.get(url) # посылаем запрос на сайт
    r.encoding = 'utf-8' # запрос раскодируем из UTF
    xml = r.text 

    root = ElementTree.fromstring(xml) # переводим в формат xml
    for i in root.findall("./item"): # поиск по xml
        answer = (i.find('title').text)
        answer += " : "
        answer += (i.find('description').text) # формируем ответ
        bot.send_message(message.chat.id, answer) # telegram ответ

bot.polling(none_stop=True) # состояние работы

