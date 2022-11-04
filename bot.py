import telebot, config
from googletrans import Translator
import languages_keyboard

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
            elif message.text == 'different':
                bot.send_message(message.chat.id, 'select new language please', reply_markup=config.eng_different_lang_buttons1)
                language_set = True
            else: # if user don't choose language from buttons, bot will ask user to write a language 
                for key, msg in languages_keyboard.ENG_LANGUAGES.items():
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False: 
                        # if message in dictionary's keys or dictionary's values, language sets
                        language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in languages_keyboard.UKR_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in languages_keyboard.RUS_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[key].title()}</b> встановлена.',
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
        elif message.text == 'Параметри ⚙️':
            bot.send_message(message.chat.id, config.ukrainian[12], reply_markup=config.ukr_options_menu)
        elif message.text == 'Параметры ⚙️':
            bot.send_message(message.chat.id, config.russian[12], reply_markup=config.rus_options_menu)
        elif message.text == 'Options ⚙️':
            bot.send_message(message.chat.id, config.english[12], reply_markup=config.eng_options_menu)
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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global language_set, reset_language, language
    if call.message:
        if call.data == 'switch_second':
            language_set = False
            reset_language = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id, config.english[7])
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, config.russian[7])
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, config.ukrainian[7])
        elif call.data == 'switch_interface':
            if config.interface == 'english':
                bot.send_message(call.message.chat.id, config.english[9], reply_markup=config.interface_language)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, config.russian[9], reply_markup=config.interface_language)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, config.ukrainian[9], reply_markup=config.interface_language)
        elif call.data == 'next':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons2)
        elif call.data == 'next2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons3)
        elif call.data == 'next3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons4)
        elif call.data == 'back':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons1)
        elif call.data == 'back2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons2)
        elif call.data == 'back3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons3)
        elif call.data == 'af':
            language = 'afrikaans'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sq':
            language = 'albanian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'am':
            language = 'amharic'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ar':
            language = 'arabic'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'hy':
            language = 'armenian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'az':
            language = 'azerbaijani'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'eu':
            language = 'basque'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'be':
            language = 'belarusian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'bn':
            language = 'bengali'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'bs':
            language = 'bosnian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'bg':
            language = 'bulgarian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ca':
            language = 'catalan'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ceb':
            language = 'cebuano'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ny':
            language = 'chichewa'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'zh-cn':
            language = 'chinese (simplified)'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'zh-tw':
            language = 'chinese (traditional)'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'co':
            language = 'corsican'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'hr':
            language = 'croatian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'cs':
            language = 'czech'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'da':
            language = 'danish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'nl':
            language = 'dutch'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'en':
            language = 'english'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'eo':
            language = 'esperanto'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'et':
            language = 'estonian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'tl':
            language = 'filipino'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'fi':
            language = 'finnish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'fr':
            language = 'french'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'fy':
            language = 'frisian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'gl':
            language = 'galician'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ka':
            language = 'georgian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'de':
            language = 'german'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'el':
            language = 'greek'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'gu':
            language = 'gujarati'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ht':
            language = 'haitian creole'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ha':
            language = 'hausa'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'haw':
            language = 'hawaiian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'iw':
            language = 'hebrew'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'he':
            language = 'hebrew'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'hi':
            language = 'hindi'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'hmn':
            language = 'hmong'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'hu':
            language = 'hungarian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'is':
            language = 'icelandic'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ig':
            language = 'igbo'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'id':
            language = 'indonesian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ga':
            language = 'irish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'it':
            language = 'italian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ja':
            language = 'japanese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'jw':
            language = 'javanese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'kn':
            language = 'kannada'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'kk':
            language = 'kazakh'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'km':
            language = 'khmer'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ko':
            language = 'korean'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ku':
            language = 'kurdish (kurmanji)'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ky':
            language = 'kyrgyz'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'lo':
            language = 'lao'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'la':
            language = 'latin'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'lv':
            language = 'latvian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'lt':
            language = 'lithuanian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'lb':
            language = 'luxembourgish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mk':
            language = 'macedonian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mg':
            language = 'malagasy'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ms':
            language = 'malay'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ml':
            language = 'malayalam'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mt':
            language = 'maltese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mi':
            language = 'maori'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mr':
            language = 'marathi'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'mn':
            language = 'mongolian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'my':
            language = 'myanmar (burmese)'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ne':
            language = 'nepali'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'no':
            language = 'norwegian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'or':
            language = 'odia'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ps':
            language = 'pashto'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'fa':
            language = 'persian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'pl':
            language = 'polish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'pt':
            language = 'portuguese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'pa':
            language = 'punjabi'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ro':
            language = 'romanian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ru':
            language = 'russian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sm':
            language = 'samoan'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'gd':
            language = 'scots gaelic'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sr':
            language = 'serbian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'st':
            language = 'sesotho'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sn':
            language = 'shona'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sd':
            language = 'sindhi'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'si':
            language = 'sinhala'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sk':
            language = 'slovak'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sl':
            language = 'slovenian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'so':
            language = 'somali'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'es':
            language = 'spanish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'su':
            language = 'sundanese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sw':
            language = 'swahili'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'sv':
            language = 'swedish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'tg':
            language = 'tajik'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ta':
            language = 'tamil'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'te':
            language = 'telugu'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'th':
            language = 'thai'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'tr':
            language = 'turkish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'uk':
            language = 'ukrainian'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ur':
            language = 'urdu'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'ug':
            language ='uyghur'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'uz':
            language = 'uzbek'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'vi':
            language = 'vietnamese'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'cy':
            language = 'welsh'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'xh':
            language = 'xhosa'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'yi':
            language = 'yiddish'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'yo':
            language = 'yoruba'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        elif call.data == 'zu':
            language = 'zulu'
            bot.send_message(call.message.chat.id,  f'{language.title()} set')
        
            
            

bot.infinity_polling()
