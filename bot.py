import telebot, config
from googletrans import Translator
from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
translator = Translator()
language = ''

@bot.message_handler(commands=['start'])
def welcome(message):


    bot.send_message(message.chat.id, 'Привет, я попробую перевести твои текста.')
    bot.send_message(message.chat.id, 'Чтобы я могу работать правильно, пожалуйста,'+
    ' выбери язык, на который хочешь перевести текст.', reply_markup=config.markup)

@bot.message_handler(content_types=['text'])
def language(message):
    global language
    if message.text == '🇷🇺 ru':
        language = 'ru'
        bot.send_message(message.chat.id, 'Язык перевода <b>Русский</b> установлен',
            parse_mode='html')
    elif message.text == '🇬🇧 en':
        language = 'en'
        bot.send_message(message.chat.id, 'Язык перевода <b>Английский</b> установлен',
            parse_mode='html')
    else:
        bot.send_message(message.chat.id, (translator.translate(message.text, language)).text)

bot.infinity_polling()