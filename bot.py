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
    global language_set, reset_language, language
    if call.message:
        if call.data == 'switch_second':
            language_set = False
            reset_language = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id, config.english[7], reply_markup=config.eng_different_lang_buttons1)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, config.russian[7], reply_markup=config.rus_different_lang_buttons1)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, config.ukrainian[7], reply_markup=config.ukr_different_lang_buttons1)
        elif call.data == 'switch_interface':
            if config.interface == 'english':
                bot.send_message(call.message.chat.id, config.english[9], reply_markup=config.interface_language)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, config.russian[9], reply_markup=config.interface_language)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, config.ukrainian[9], reply_markup=config.interface_language)
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
            language = 'afrikaans'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{language.title()}</b> установлен.', parse_mode='html')
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{language.title()}</b> встановлена.', parse_mode='html')
        elif call.data == 'sq':
            language = 'albanian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'am':
            language = 'amharic'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ar':
            language = 'arabic'
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b>set.', parse_mode='html')
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hy':
            language = 'armenian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'az':
            language = 'azerbaijani'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'eu':
            language = 'basque'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'be':
            language = 'belarusian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bn':
            language = 'bengali'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bs':
            language = 'bosnian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'bg':
            language = 'bulgarian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ca':
            language = 'catalan'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ceb':
            language = 'cebuano'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ny':
            language = 'chichewa'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zh-cn':
            language = 'chinese (simplified)'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zh-tw':
            language = 'chinese (traditional)'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'co':
            language = 'corsican'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hr':
            language = 'croatian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'cs':
            language = 'czech'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'da':
            language = 'danish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'nl':
            language = 'dutch'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'en':
            language = 'english'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'eo':
            language = 'esperanto'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'et':
            language = 'estonian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tl':
            language = 'filipino'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fi':
            language = 'finnish'
            reset_language = False
            language_set = True
            if config.interface== 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fr':
            language = 'french'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fy':
            language = 'frisian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gl':
            language = 'galician'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ka':
            language = 'georgian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'de':
            language = 'german'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'el':
            language = 'greek'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gu':
            language = 'gujarati'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ht':
            language = 'haitian creole'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ha':
            language = 'hausa'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'haw':
            language = 'hawaiian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'iw':
            language = 'hebrew'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'he':
            language = 'hebrew'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hi':
            language = 'hindi'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hmn':
            language = 'hmong'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'hu':
            language = 'hungarian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'is':
            language = 'icelandic'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ig':
            language = 'igbo'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'id':
            language = 'indonesian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ga':
            language = 'irish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'it':
            language = 'italian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ja':
            language = 'japanese'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'jw':
            language = 'javanese'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'kn':
            language = 'kannada'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'kk':
            language = 'kazakh'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'km':
            language = 'khmer'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ko':
            language = 'korean'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ku':
            language = 'kurdish (kurmanji)'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ky':
            language = 'kyrgyz'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lo':
            language = 'lao'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'la':
            language = 'latin'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lv':
            language = 'latvian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lt':
            language = 'lithuanian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'lb':
            language = 'luxembourgish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mk':
            language = 'macedonian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mg':
            language = 'malagasy'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ms':
            language = 'malay'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ml':
            language = 'malayalam'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mt':
            language = 'maltese'
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface== 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mi':
            language = 'maori'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mr':
            language = 'marathi'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'mn':
            language = 'mongolian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'my':
            language = 'myanmar (burmese)'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ne':
            language = 'nepali'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'no':
            language = 'norwegian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'or':
            language = 'odia'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ps':
            language = 'pashto'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'fa':
            language = 'persian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pl':
            language = 'polish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pt':
            language = 'portuguese'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'pa':
            language = 'punjabi'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ro':
            language = 'romanian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ru':
            language = 'russian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sm':
            language = 'samoan'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'gd':
            language = 'scots gaelic'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sr':
            language = 'serbian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'st':
            language = 'sesotho'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sn':
            language = 'shona'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sd':
            language = 'sindhi'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'si':
            language = 'sinhala'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sk':
            language = 'slovak'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sl':
            language = 'slovenian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'so':
            language = 'somali'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'es':
            language = 'spanish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'su':
            language = 'sundanese'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sw':
            language = 'swahili'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'sv':
            language = 'swedish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tg':
            language = 'tajik'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ta':
            language = 'tamil'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'te':
            language = 'telugu'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'th':
            language = 'thai'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'tr':
            language = 'turkish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'uk':
            language = 'ukrainian'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ur':
            language = 'urdu'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'ug':
            language ='uyghur'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'uz':
            language = 'uzbek'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'vi':
            language = 'vietnamese'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'cy':
            language = 'welsh'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'xh':
            language = 'xhosa'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'yi':
            language = 'yiddish'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'yo':
            language = 'yoruba'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        elif call.data == 'zu':
            language = 'zulu'
            reset_language = False
            language_set = True
            if config.interface == 'english':
                bot.send_message(call.message.chat.id,  f'<b>{language.title()}</b> set.', parse_mode='html', reply_markup=config.eng_menu)
            elif config.interface == 'russian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.RUS_LANGUAGES[call.data].title()}</b> установлен.', parse_mode='html', reply_markup=config.rus_menu)
            elif config.interface == 'ukrainian':
                bot.send_message(call.message.chat.id, f'<b>{languages_keyboard.UKR_LANGUAGES[call.data].title()}</b> встановлена.', parse_mode='html', reply_markup=config.ukr_menu)
        
            
            

bot.infinity_polling()
