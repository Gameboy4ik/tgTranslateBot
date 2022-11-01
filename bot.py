import telebot, config
from googletrans import Translator

bot = telebot.TeleBot(config.TOKEN, parse_mode=None) # creating bot
languages_list = config.LANGUAGES 
translator = Translator() # creating translator
language = ''
language_set = False 
restart_choosing_language = False
logged_in = False

def translating(message):
    global language, language_set
    if language_set == False: # if false user must choose the language the bot will translate into
        while language_set == False:
            # buttons with default languages
            if message.text == '🇷🇺 RU': 
                language = 'ru'
                bot.send_message(message.chat.id, 'Язык перевода <b>Русский</b> установлен',
                    parse_mode='html', reply_markup=config.menu)
                language_set = True
            elif message.text == '🇬🇧 EN':
                language = 'en'
                bot.send_message(message.chat.id, 'Язык перевода <b>Английский</b> установлен',
                    parse_mode='html', reply_markup=config.menu)
                language_set = True
            elif message.text == '🇺🇦 UA':
                language = 'uk'
                bot.send_message(message.chat.id, 'Язык перевода <b>Украинский</b> установлен.',
                    parse_mode='html', reply_markup=config.menu)
                language_set = True
            else: # if user don't choose language from buttons, bot will ask user to write a language 
                for key, msg in languages_list.items():
                    if msg == message.text.lower() or key == message.text.lower(): 
                        # if message in dictionary's keys or dictionary's values, language sets
                        language = languages_list[key]
                        bot.send_message(message.chat.id, f'<b>{language.title()}</b> установлен.',
                            parse_mode='html', reply_markup=config.menu)
                        language_set = True
                if language_set == False and logged_in == True: # if message not in dictionary, while restart
                    bot.send_message(message.chat.id, 'Такого языка нет в нашей базе данных.'+
                        ' Попробуйте ещё раз.')
                    break
    else: # if language already installed, bot just translate message and reply
        if message.text == 'Choose Different Language':
            language_set = False
            bot.send_message(message.chat.id, 'Введите новый язык.')
        else:
            bot.send_message(message.chat.id,
                (translator.translate(message.text, language)).text)

@bot.message_handler(commands=['start'])
def welcome(message): # welcome function
    bot.send_message(message.chat.id,
        "🇬🇧 Choose the interface language:\n🇺🇦 Виберіть мову інтерфейсу:\n🇷🇺 Выберите язык интерфейса:",
        reply_markup=config.interface_language)



@bot.message_handler(content_types=['text'])
def interface(message):
    if message.text == '🇷🇺 Русский':
        config.interface = 'russian'
        bot.send_message(message.chat.id, "Привет, я попробую перевести твои сообщения.")
        bot.send_message(message.chat.id, "Чтобы я мог работать правильно, пожалуйста,"+
            " выберите язык, на который хотите перевести текст.", reply_markup=config.start_markup)
        bot.send_message(message.chat.id, "<b>P.S:</b> Если нужного вам языка не оказалось"+
            " в вариантах ответа, пожалуйста, введите язык в сообщении и я постараюсь найти его.",
            parse_mode='html')
        logged_in = True
    elif message.text == '🇬🇧 English':
        config.interface = 'english'
        bot.send_message(message.chat.id, "Hello, I'll try to translate your messages.")
        bot.send_message(message.chat.id, "So that I can work correctly, please select"+
            " the language you want to translate into.", reply_markup=config.start_markup)
        bot.send_message(message.chat.id, "<b>P.S:</b> If the language you need is not in"+
            " the answer options, please enter the language in the message and I'll try to find it.",
            parse_mode='html')
        logged_in = True
    elif message.text == '🇺🇦 Українська':
        config.interface = 'ukrainian'
        bot.send_message(message.chat.id, "Привіт, я спробую перекласти твої повідомлення.")
        bot.send_message(message.chat.id, "Щоб я міг працювати правильно, будь ласка,"+
            " оберіть мову, на яку хочете перекласти текст.", reply_markup=config.start_markup)
        bot.send_message(message.chat.id, "<b>P.S:</b> Якщо потрібної вам мови не виявилося"+
            " в варіантах відповіді, будь ласка, введіть мову в повідомлені і я постараюся знайти її.",
            parse_mode='html')
        logged_in = True
    translating(message)


bot.infinity_polling()
