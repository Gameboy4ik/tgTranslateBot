import telebot, config
from googletrans import Translator
import languages_keyboard

bot = telebot.TeleBot(config.TOKEN, parse_mode=None) # creating bot
translator = Translator() # creating translator
language_set = False 
reset_language = False
switching_first = False
switching_second = True

def translating(message):
    global language_set, reset_language
    if language_set == False: # if false user must choose the language the bot will translate into
        while language_set == False:
            # buttons with default languages
            if message.text == '🇷🇺 RU': 
                config.second_language = 'ru'
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
                config.second_language = 'en'
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
                config.second_language = 'uk'
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
            elif message.text == '...':
                if config.interface == 'english':
                    bot.send_message(message.chat.id, 'Select new language please', reply_markup=config.eng_different_lang_buttons1)
                elif config.interface == 'russian':
                    bot.send_message(message.chat.id, 'Выберите новый язык пожалуйста', reply_markup=config.rus_different_lang_buttons1)
                elif config.interface == 'ukrainian':
                    bot.send_message(message.chat.id, 'Виберіть нову мову будь ласка', reply_markup=config.ukr_different_lang_buttons1)
                language_set = True
            else: # if user don't choose language from buttons, bot will ask user to write a language 
                for key, msg in languages_keyboard.ENG_LANGUAGES.items():
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False: 
                        # if message in dictionary's keys or dictionary's values, language sets
                        config.second_language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{config.second_language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in languages_keyboard.UKR_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        config.second_language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{config.second_language.title()}</b> set.',
                                parse_mode='html', reply_markup=config.eng_menu)
                        elif config.interface == 'ukrainian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[key].title()}</b> встановлена.',
                                parse_mode='html', reply_markup=config.ukr_menu)
                        language_set = True
                        break
                for key, msg in languages_keyboard.RUS_LANGUAGES.items(): # like ENG
                    if msg == message.text.lower() or key == message.text.lower() and language_set == False:
                        config.second_language = languages_keyboard.ENG_LANGUAGES[key]
                        if config.interface == 'russian':
                            bot.send_message(message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[key].title()}</b> установлен.',
                                parse_mode='html', reply_markup=config.rus_menu)
                        elif config.interface == 'english':
                            bot.send_message(message.chat.id, f'<b>{config.second_language.title()}</b> set.',
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
            bot.send_message(message.chat.id, config.english[7], reply_markup=config.eng_different_lang_buttons1)
        elif message.text == config.russian[6]:
            language_set = False
            reset_language = True
            bot.send_message(message.chat.id, config.russian[7], reply_markup=config.rus_different_lang_buttons1)
        elif message.text == config.ukrainian[6]:
            language_set = False
            reset_language = True
            bot.send_message(message.chat.id, config.ukrainian[7], reply_markup=config.ukr_different_lang_buttons1)
        if message.text == config.english[8]:
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
            if config.first_language == 'auto':
                bot.send_message(message.chat.id,
                    (translator.translate(message.text, languages_keyboard.ENG_LANGUAGES[config.second_language])).text)
            else:
                bot.send_message(message.chat.id,
                    (translator.translate(message.text, languages_keyboard.ENG_LANGUAGES[config.second_language], languages_keyboard.ENG_LANGUAGES[config.first_language])).text)

@bot.message_handler(commands=['start'])
def welcome(message): # welcome function
    global language_set
    config.second_language = ''
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
        else:
            bot.send_message(message.chat.id, config.russian[10], reply_markup=config.rus_menu)
    elif message.text == '🇬🇧 English': # interface changing on english
        config.interface = 'english'
        if language_set == False:
            bot.send_message(message.chat.id, "Hello, I'll try to translate your messages.")
            bot.send_message(message.chat.id, "So that I can work correctly, please select"+
                " the language you want to translate into.", reply_markup=config.start_markup)
        else:
            bot.send_message(message.chat.id, config.english[10], reply_markup=config.eng_menu)
    elif message.text == '🇺🇦 Українська': # interface changing on ukrainian
        config.interface = 'ukrainian'
        if language_set == False:
            bot.send_message(message.chat.id, "Привіт, я спробую перекласти твої повідомлення.")
            bot.send_message(message.chat.id, "Щоб я міг працювати правильно, будь ласка,"+
                " оберіть мову, на яку хочете перекласти текст.", reply_markup=config.start_markup)
        else:
            bot.send_message(message.chat.id, config.ukrainian[10], reply_markup=config.ukr_menu)
    translating(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global language_set, reset_language, switching_first, switching_second
    if call.message:
        if call.data == 'switch_second':
            language_set = False
            reset_language = True
            if config.interface == 'english':
                bot.edit_message_text(config.english[7], call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons1)
            elif config.interface == 'russian':
                bot.edit_message_text(config.russian[7], call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons1)
            elif config.interface == 'ukrainian':
                bot.edit_message_text(config.ukrainian[7], call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons1)
        elif call.data == 'switch_interface':
            if config.interface == 'english':
                bot.send_message(call.message.chat.id, config.english[9], reply_markup=config.interface_language)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, config.russian[9], reply_markup=config.interface_language)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, config.ukrainian[9], reply_markup=config.interface_language)
        elif call.data == 'switch_both':
            if config.interface == 'english':
                bot.edit_message_text(f'first: {config.first_language}\nsecond: {config.second_language}', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_both_languages)
            elif config.interface == 'russian':
                bot.edit_message_text(f'первый: {config.first_language}\nвторой: {config.second_language}', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_both_languages)
            elif config.interface == 'ukrainian':
                bot.edit_message_text(f'перший: {config.first_language}\nдругий: {config.second_language}', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_both_languages)
        elif call.data == 'switch_first':
            switching_first = True
            switching_second = False
            bot.send_message(call.message.chat.id, 'choose first', reply_markup=config.eng_different_lang_buttons1)
        elif call.data == 'swtich_second':
            switching_first = False
            switching_second = True
            bot.send_message(call.message.chat.id, 'choose second', reply_markup=config.eng_different_lang_buttons1)
        elif call.data == 'eng_next':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons2)
        elif call.data == 'eng_next2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons3)
        elif call.data == 'eng_next3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons4)
        elif call.data == 'eng_back':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons1)
        elif call.data == 'eng_back2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons2)
        elif call.data == 'eng_back3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons3)
        elif call.data == 'rus_next':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons2)
        elif call.data == 'rus_next2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons3)
        elif call.data == 'rus_next3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons4)
        elif call.data == 'rus_back':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons1)
        elif call.data == 'rus_back2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons2)
        elif call.data == 'rus_back3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons3)
        elif call.data == 'ukr_next':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons2)
        elif call.data == 'ukr_next2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons3)
        elif call.data == 'ukr_next3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons4)
        elif call.data == 'ukr_back':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons1)
        elif call.data == 'ukr_back2':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons2)
        elif call.data == 'ukr_back3':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons3)
        elif call.data == 'af':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sq':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'am':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ar':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{config.second_language.title()}</b>set.', parse_mode='html')
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hy':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'az':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'eu':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'be':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bs':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bg':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ca':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ceb':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ny':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zh-cn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zh-tw':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'co':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hr':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'cs':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'da':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'nl':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'en':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'eo':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'et':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tl':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fi':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface== 'english':
                bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fr':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fy':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gl':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ka':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'de':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'el':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gu':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ht':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ha':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'haw':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'iw':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'he':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hi':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hmn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hu':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'is':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ig':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'id':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html',reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ga':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'it':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ja':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'jw':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'kn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'kk':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'km':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ko':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ku':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ky':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lo':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'la':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lv':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lt':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lb':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mk':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mg':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ms':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ml':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mt':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface== 'ukrainian':
                bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mi':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mr':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'my':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ne':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'no':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'or':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ps':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fa':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pl':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pt':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pa':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ro':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ru':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sm':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gd':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sr':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'st':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sn':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sd':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'si':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sk':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sl':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'so':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'es':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'su':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sw':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sv':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tg':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ta':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'te':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'th':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tr':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'uk':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ur':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ug':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'uz':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'vi':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'cy':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'xh':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'yi':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'yo':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zu':
            if switching_second == True:
                config.second_language = call.data
            if switching_first == True:
                config.first_language = call.data
                switching_first = False
                switching_second = True
            reset_language = False
            language_set = True
            if config.interface == 'english':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Translation <b>Auto - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Translation <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()} - {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id,  f'Перевод <b>Авто - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
                else:
                    bot.send_message(call.message.chat.id,  f'Перевод <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()} - {languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.send_message(call.message.chat.id, f'Переклад <b>Авто - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
                else:
                    bot.send_message(call.message.chat.id, f'Переклад <b>{language_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        
            
            

bot.infinity_polling()
