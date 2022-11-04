from telebot import types
import languages_keyboard

TOKEN = '5433231218:AAGPfD0VW_iVM722S5MLxLiTQRS7X4ET8nQ' # bot token

ukrainian = {
    1:'Мова перекладу <b>Російська</b> встановлена.',
    2:'Мова перекладу <b>Англійська</b> встановлена.',
    3:'Мова перекладу <b>Українська</b> встановлена.',
    # 4:f'<b>{language.title()}</b> встановлен.',
    5:'Такої мови немає в нашій базі даних. Спробуйте ще раз.',
    6:'Виберіть іншу мову',
    7:'Введіть іншу мову.',
    8:'Змінити мову інтерфейсу',
    9:'Виберіть іншу мову інтерфейсу:',
    10:'Мова інтерфейсу змінена.',
    11:'Самостійно вибрати початкову та остаточну мову',
    12:'Параметри ⚙️',
}

russian = {
    1:'Язык перевода <b>Русский</b> установлен.',
    2:'Язык перевода <b>Английский</b> установлен.',
    3:'Язык перевода <b>Украинский</b> установлен.',
    # 4:f'<b>{language.title()}</b> установлен.',
    5:'Такого языка нет в нашей базе данных. Попробуйте ещё раз.',
    6:'Выберите другой язык',
    7:'Введите другой язык.',
    8:'Сменить язык интерфейса',
    9:'Выберите другой язык интерфейса:',
    10:'Язык интерфейса изменён.',
    11:'Самостоятельно выбрать начальный и окончательный язык',
    12:'Параметры ⚙️',
}

english = {
    1:'Translation language <b>Russian</b> is set.',
    2:'Translation language <b>English</b> is set.',
    3:'Translation language <b>Ukrainian</b> is set.',
    # 4:f'<b>{language.title()}</b> set.',
    5:'This language is not in our database. Try again.',
    6:'Select another language',
    7:'Enter another language.',
    8:'Change interface language',
    9:'Select another interface language:',
    10:'Interface language changed.',
    11:'Independently choose the initial and final language',
    12:'Options ⚙️',
}

interface = None
interfaced = False

interface_language = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
ru_interface_lang = types.KeyboardButton('🇷🇺 Русский')
en_interface_lang = types.KeyboardButton('🇬🇧 English')
ua_interface_lang = types.KeyboardButton('🇺🇦 Українська')
interface_language.add(en_interface_lang, ua_interface_lang, ru_interface_lang)

start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
ru_lang = types.KeyboardButton('🇷🇺 RU')
en_lang = types.KeyboardButton('🇬🇧 EN')
ua_lang = types.KeyboardButton('🇺🇦 UA')
different_lang = types.KeyboardButton('different')
start_markup.add(en_lang, ua_lang, ru_lang, different_lang)

ukr_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
ukr_options = types.KeyboardButton(ukrainian[12])
ukr_menu.add(ukr_options)

ukr_options_menu = types.InlineKeyboardMarkup(row_width=1)
ukr_different_lang = types.InlineKeyboardButton(ukrainian[6], callback_data='switch_second')
ukr_different_interface_lang = types.InlineKeyboardButton(ukrainian[8], callback_data='switch_interface')
# ukr_different_both_lang = types.InlineKeyboardButton(ukrainian[11], callback_data='switch_both')
ukr_options_menu.add(ukr_different_lang, ukr_different_interface_lang)

rus_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
rus_options = types.KeyboardButton(russian[12])
rus_menu.add(rus_options)

rus_options_menu = types.InlineKeyboardMarkup(row_width=1)
rus_different_lang = types.InlineKeyboardButton(russian[6], callback_data='switch_second')
rus_different_interface_lang = types.InlineKeyboardButton(russian[8], callback_data='switch_interface')
# rus_different_both_lang = types.InlineKeyboardButton(russian[11], callback_data='switch_both')
rus_options_menu.add(rus_different_lang, rus_different_interface_lang)

eng_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
eng_options = types.KeyboardButton(english[12])
eng_menu.add(eng_options)

eng_options_menu = types.InlineKeyboardMarkup(row_width=1)
eng_different_lang = types.InlineKeyboardButton(english[6], callback_data='switch_second')
eng_different_interface_lang = types.InlineKeyboardButton(english[8], callback_data='switch_interface')
# eng_different_both_lang = types.InlineKeyboardButton(english[11], callback_data='switch_both')
eng_options_menu.add(eng_different_lang, eng_different_interface_lang)


eng_different_lang_buttons1 = types.InlineKeyboardMarkup(row_width=3)
eng_next_btn1 = types.InlineKeyboardButton('next', callback_data='next')
eng_different_lang_buttons1.add(
    languages_keyboard.btn0,
    languages_keyboard.btn1,
    languages_keyboard.btn2,
    languages_keyboard.btn3,
    languages_keyboard.btn4,
    languages_keyboard.btn5,
    languages_keyboard.btn6,
    languages_keyboard.btn7,
    languages_keyboard.btn8,
    languages_keyboard.btn9,
    languages_keyboard.btn10,
    languages_keyboard.btn11,
    languages_keyboard.btn12,
    languages_keyboard.btn13,
    languages_keyboard.btn14,
    languages_keyboard.btn15,
    languages_keyboard.btn16,
    languages_keyboard.btn17,
    languages_keyboard.btn18,
    languages_keyboard.btn19,
    languages_keyboard.btn20,
    languages_keyboard.btn21,
    languages_keyboard.btn22,
    languages_keyboard.btn23,
    languages_keyboard.btn24,
    languages_keyboard.btn25,
    languages_keyboard.btn26,
    languages_keyboard.btn27,
    languages_keyboard.btn28,
    languages_keyboard.btn29,
    languages_keyboard.btn30,
    eng_next_btn1
)

eng_different_lang_buttons2 = types.InlineKeyboardMarkup(row_width=3)
eng_next_btn2 = types.InlineKeyboardButton('next', callback_data='next2')
eng_back_btn = types.InlineKeyboardButton('back', callback_data='back')
eng_different_lang_buttons2.add(
    languages_keyboard.btn31,
    languages_keyboard.btn32,
    languages_keyboard.btn33,
    languages_keyboard.btn34,
    languages_keyboard.btn35,
    languages_keyboard.btn36,
    languages_keyboard.btn37,
    languages_keyboard.btn38,
    languages_keyboard.btn39,
    languages_keyboard.btn40,
    languages_keyboard.btn41,
    languages_keyboard.btn42,
    languages_keyboard.btn43,
    languages_keyboard.btn44,
    languages_keyboard.btn45,
    languages_keyboard.btn46,
    languages_keyboard.btn47,
    languages_keyboard.btn48,
    languages_keyboard.btn49,
    languages_keyboard.btn50,
    languages_keyboard.btn51,
    languages_keyboard.btn52,
    languages_keyboard.btn53,
    languages_keyboard.btn54,
    languages_keyboard.btn55,
    languages_keyboard.btn56,
    languages_keyboard.btn57,
    languages_keyboard.btn58,
    languages_keyboard.btn59,
    languages_keyboard.btn60,
    eng_back_btn,
    eng_next_btn2
)

eng_different_lang_buttons3 = types.InlineKeyboardMarkup(row_width=3)
eng_next_btn3 = types.InlineKeyboardButton('next', callback_data='next3')
eng_back_btn2 = types.InlineKeyboardButton('back', callback_data='back2')
eng_different_lang_buttons3.add(
    languages_keyboard.btn61,
    languages_keyboard.btn62,
    languages_keyboard.btn63,
    languages_keyboard.btn64,
    languages_keyboard.btn65,
    languages_keyboard.btn66,
    languages_keyboard.btn67,
    languages_keyboard.btn68,
    languages_keyboard.btn69,
    languages_keyboard.btn70,
    languages_keyboard.btn71,
    languages_keyboard.btn72,
    languages_keyboard.btn73,
    languages_keyboard.btn74,
    languages_keyboard.btn75,
    languages_keyboard.btn76,
    languages_keyboard.btn77,
    languages_keyboard.btn78,
    languages_keyboard.btn79,
    languages_keyboard.btn80,
    languages_keyboard.btn81,
    languages_keyboard.btn82,
    languages_keyboard.btn83,
    languages_keyboard.btn84,
    languages_keyboard.btn85,
    languages_keyboard.btn86,
    languages_keyboard.btn87,
    languages_keyboard.btn88,
    languages_keyboard.btn89,
    languages_keyboard.btn90,
    eng_back_btn2,
    eng_next_btn3
)

eng_different_lang_buttons4 = types.InlineKeyboardMarkup(row_width=3)
eng_back_btn3 = types.InlineKeyboardButton('back', callback_data='back3')
eng_different_lang_buttons4.add(
    languages_keyboard.btn91,
    languages_keyboard.btn92,
    languages_keyboard.btn93,
    languages_keyboard.btn94,
    languages_keyboard.btn95,
    languages_keyboard.btn96,
    languages_keyboard.btn97,
    languages_keyboard.btn98,
    languages_keyboard.btn99,
    languages_keyboard.btn100,
    languages_keyboard.btn101,
    languages_keyboard.btn102,
    languages_keyboard.btn103,
    languages_keyboard.btn104,
    languages_keyboard.btn105,
    eng_back_btn3,
    languages_keyboard.btn106,
)

