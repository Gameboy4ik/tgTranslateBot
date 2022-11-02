import telebot, config
from googletrans import Translator

bot = telebot.TeleBot(config.TOKEN, parse_mode=None) # creating bot
translator = Translator() # creating translator
language = ''
language_set = False 
reset_language = False

def translating(message):
    global language, language_set, reset_language
    if language_set == False: # if false user must choose the language the bot will translate into
        while language_set == False:
            # buttons with default languages
            if message.text == '🇷🇺 RU': 
                language = 'ru'
                if config.interface == 'russian':
                    bot.send_message(message.chat.id, config.russian[1],
                        parse_mode='html', reply_markup=config.rus_menu)
                elif config.interface == 'english':
                    bot.send_message(message.chat.id, config.english[1],
                        parse_mode='html', reply_markup=config.eng_menu)
                elif config.interface == 'ukrainian':
                    bot.send_message(message.chat.id, config.ukrainian[1],
                        parse_mode='html', reply_markup=config.ukr_menu)
                language_set = True
            elif message.text == '🇬🇧 EN':
                language = 'en'
                if config.interface == 'russian':
                    bot.send_message(message.chat.id, config.russian[2],
                        parse_mode='html', reply_markup=config.rus_menu)
                elif config.interface == 'english':
                    bot.send_message(message.chat.id, config.english[2],
                        parse_mode='html', reply_markup=config.eng_menu)
                elif config.interface == 'ukrainian':
                    bot.send_message(message.chat.id, config.ukrainian[2],
                        parse_mode='html', reply_markup=config.ukr_menu)
                language_set = True
            elif message.text == '🇺🇦 UA':
                language = 'uk'
                if config.interface == 'russian':
                    bot.send_message(message.chat.id, config.russian[3],
                        parse_mode='html', reply_markup=config.rus_menu)
                elif config.interface == 'english':
                    bot.send_message(message.chat.id, config.english[3],
                        parse_mode='html', reply_markup=config.eng_menu)
                elif config.interface == 'ukrainian':
                    bot.send_message(message.chat.id, config.ukrainian[3],
                        parse_mode='html', reply_markup=config.ukr_menu)
                language_set = True
            else: # if user don't choose language from buttons, bot will ask user to write a language 
                for key, msg in config.ENG_LANGUAGES.items():
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False: 
                        # if message in dictionary's keys or dictionary's values, language sets
                        language = config.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{config.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{config.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in config.UKR_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        language = config.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{config.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{config.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in config.RUS_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        language = config.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{config.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{config.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                if language_set == False and reset_language == True: # if message not in dictionary, while restart
                    if config.interface == 'russian':
                        bot.send_message(message.chat.id, config.russian[5])
                        break
                    elif config.interface == 'english':
                        bot.send_message(message.chat.id, config.english[5])
                        break
                    elif config.interface == 'ukrainian':
                        bot.send_message(message.chat.id, config.ukrainian[5])
                        break
    else: # if language already installed, bot just translate message and reply
        if message.text == config.english[6]:
            language_set = False
            reset_language = True
            bot.send_message(message.chat.id, config.english[7])
        elif message.text == config.russian[6]:
            language_set = False
            reset_language = True
            bot.send_message(message.chat.id, config.russian[7])
        elif message.text == config.ukrainian[6]:
            language_set = False
            reset_language = True
            bot.send_message(message.chat.id, config.ukrainian[7])
        elif message.text == config.english[8]:
            bot.send_message(message.chat.id, config.english[9], reply_markup=config.interface_language)
        elif message.text == config.russian[8]:
            bot.send_message(message.chat.id, config.russian[9], reply_markup=config.interface_language)
        elif message.text == config.ukrainian[8]:
            bot.send_message(message.chat.id, config.ukrainian[9], reply_markup=config.interface_language)
        elif message.text == '🇷🇺 Русский' or message.text == '🇬🇧 English' or message.text == '🇺🇦 Українська':
            pass
        else:
            bot.send_message(message.chat.id,
                (translator.translate(message.text, language)).text)

@bot.message_handler(commands=['start'])
def welcome(message): # welcome function
    global language, language_set
    language = ''
    language_set = False
    bot.send_message(message.chat.id,
        "🇬🇧 Choose the interface language:\n🇺🇦 Виберіть мову інтерфейсу:\n🇷🇺 Выберите язык интерфейса:",
        reply_markup=config.interface_language)



@bot.message_handler(content_types=['text'])
def interface(message):
    global logged_in
    if message.text == '🇷🇺 Русский': # interface changing on russian
        config.interface = 'russian'
        if language_set == False:
            bot.send_message(message.chat.id, "Привет, я попробую перевести твои сообщения.")
            bot.send_message(message.chat.id, "Чтобы я мог работать правильно, пожалуйста,"+
                " выберите язык, на который хотите перевести текст.", reply_markup=config.start_markup)
            bot.send_message(message.chat.id, "<b>P.S:</b> Если нужного вам языка не оказалось"+
                " в вариантах ответа, пожалуйста, введите язык в сообщении и я постараюсь найти его.",
                parse_mode='html')
        else:
            bot.send_message(message.chat.id, config.russian[10], reply_markup=config.rus_menu)
    elif message.text == '🇬🇧 English': # interface changing on english
        config.interface = 'english'
        if language_set == False:
            bot.send_message(message.chat.id, "Hello, I'll try to translate your messages.")
            bot.send_message(message.chat.id, "So that I can work correctly, please select"+
                " the language you want to translate into.", reply_markup=config.start_markup)
            bot.send_message(message.chat.id, "<b>P.S:</b> If the language you need is not in"+
                " the answer options, please enter the language in the message and I'll try to find it.",
                parse_mode='html')
        else:
            bot.send_message(message.chat.id, config.english[10], reply_markup=config.eng_menu)
    elif message.text == '🇺🇦 Українська': # interface changing on ukrainian
        config.interface = 'ukrainian'
        if language_set == False:
            bot.send_message(message.chat.id, "Привіт, я спробую перекласти твої повідомлення.")
            bot.send_message(message.chat.id, "Щоб я міг працювати правильно, будь ласка,"+
                " оберіть мову, на яку хочете перекласти текст.", reply_markup=config.start_markup)
            bot.send_message(message.chat.id, "<b>P.S:</b> Якщо потрібної вам мови не виявилося"+
                " в варіантах відповіді, будь ласка, введіть мову в повідомлені і я постараюся знайти її.",
                parse_mode='html')
        else:
            bot.send_message(message.chat.id, config.ukrainian[10], reply_markup=config.ukr_menu)
    translating(message)


bot.infinity_polling()
