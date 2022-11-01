from ast import parse
import telebot, config
from googletrans import Translator
from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None) # creating bot
languages_list = config.LANGUAGES 
translator = Translator() # creating translator
language = ''
language_set = False 

@bot.message_handler(commands=['start'])
def welcome(message): # welcome function


    bot.send_message(message.chat.id, 'Привет, я попробую перевести твои текста.')
    bot.send_message(message.chat.id, 'Чтобы я мог работать правильно, пожалуйста,'+
        ' выбери язык, на который хочешь перевести текст.', reply_markup=config.markup)
    bot.send_message(message.chat.id, '<b>P.S:</b> Если нужного вам языка не оказалось'+
        ' в вариантах ответа, пожалуйста, введите язык в сообщении и мы постараемся найти его.',
        parse_mode='html')

@bot.message_handler(content_types=['text'])
def translating(message):
    global language, language_set
    if language_set == False: # if false user must choose the language the bot will translate into
        while language_set == False:
            # buttons with default languages
            if message.text == '🇷🇺 ru': 
                language = 'ru'
                bot.send_message(message.chat.id, 'Язык перевода <b>Русский</b> установлен',
                    parse_mode='html')
                language_set = True
            elif message.text == '🇬🇧 en':
                language = 'en'
                bot.send_message(message.chat.id, 'Язык перевода <b>Английский</b> установлен',
                    parse_mode='html')
                language_set = True
            else: # if user don't choose language from buttons, bot will ask user to write a language 
                for key, msg in languages_list.items():
                    if msg == message.text or key == message.text: 
                        # if message in dictionary's keys or dictionary's values, language sets
                        language = languages_list[key]
                        bot.send_message(message.chat.id, f'<b>{language.title()}</b> установлен.',
                            parse_mode='html')
                        language_set = True
                    # else:
                    #     bot.send_message(message.chat.id, 'Такого языка нет в нашей базе данных.'+
                    #         ' Попробуйте ещё раз.')
                    #     break
                    # break      
    else: # if language already installed, bot just translate message and reply
        bot.send_message(message.chat.id,
            (translator.translate(message.text, language)).text)

bot.infinity_polling()
