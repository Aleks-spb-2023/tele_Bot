import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b
from loguru import logger





API_key = '5863089905:AAEtfzoclBXLFSVN3rZrFMm5HYjt8CmnlKI'
bot = telebot.TeleBot(API_key)



@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет,  {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id,  mess)



@bot.message_handler()
def get_user_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, "И тебе Привет дружок ", parse_mode='html')
    elif message.text == 'фото':
        photo = open('329765-bigthumbnail.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю ! ", parse_mode='html')




bot.polling(none_stop=True)


# # logger.debug("hello (debug)")
# # logger.info("hello (info)")
# # logger.error("hello (error)")
# logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')