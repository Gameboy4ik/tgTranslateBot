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
    global language_set, reset_language, switching_first, switching_second
    config.second_language = ''
    config.first_language = 'auto'
    language_set = False 
    reset_language = False
    switching_first = False
    switching_second = True
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
                if config.first_language == 'auto':
                    bot.edit_message_text(f'First: <b>Auto</b>\nSecond: {languages_keyboard.ENG_LANGUAGES[config.second_language].title()}', call.message.chat.id, call.message.message_id, parse_mode='html')
                else:
                    bot.edit_message_text(f'First: <b>{languages_keyboard.ENG_LANGUAGES[config.first_language].title()}</b>\nSecond: <b>{languages_keyboard.ENG_LANGUAGES[config.second_language].title()}</b>', call.message.chat.id, call.message.message_id, parse_mode='html')
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_both_languages)
            elif config.interface == 'russian':
                if config.first_language == 'auto':
                    bot.edit_message_text(f'Первый: <b>Авто</b>\nВторой: <b>{languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b>', call.message.chat.id, call.message.message_id, parse_mode='html')
                else:
                    bot.edit_message_text(f'Первый: <b>{languages_keyboard.RUS_LANGUAGES[config.first_language].title()}</b>\nВторой: <b>{languages_keyboard.RUS_LANGUAGES[config.second_language].title()}</b>', call.message.chat.id, call.message.message_id, parse_mode='html')
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_both_languages)
            elif config.interface == 'ukrainian':
                if config.first_language == 'auto':
                    bot.edit_message_text(f'Перший: <b>Авто</b>\nДругий: <b>{languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b>', call.message.chat.id, call.message.message_id, parse_mode='html')
                else:
                    bot.edit_message_text(f'Перший: <b>{languages_keyboard.UKR_LANGUAGES[config.first_language].title()}</b>\nДругий: <b>{languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b>', call.message.chat.id, call.message.message_id, parse_mode='html')
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_both_languages)
        elif call.data == 'switch_first':
            switching_first = True
            switching_second = False
            if config.interface == 'english':
                bot.edit_message_text('Choose first:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons1)
            elif config.interface == 'russian':
                bot.edit_message_text('Выберите первый:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons1)
            elif config.interface == 'ukrainian':
                bot.edit_message_text('Виберіть першу:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons1)
        elif call.data == 'swtich_second':
            switching_first = False
            switching_second = True
            if config.interface == 'english':
                bot.edit_message_text('Choose second:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.eng_different_lang_buttons1)
            elif config.interface == 'russian':
                bot.edit_message_text('Выберите второй:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.rus_different_lang_buttons1)
            elif config.interface == 'ukrainian':
                bot.edit_message_text('Виберіть другу:', call.message.chat.id, call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.ukr_different_lang_buttons1)
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
        elif call.data in languages_keyboard.ENG_LANGUAGES.keys():
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
                    bot.send_message(call.message.chat.id, f'Переклад <b>{languages_keyboard.UKR_LANGUAGES[config.first_language].title()} - {languages_keyboard.UKR_LANGUAGES[config.second_language].title()}</b> встановлен.', parse_mode='html', reply_markup=config.ukr_menu)
        
            
            

bot.infinity_polling()
