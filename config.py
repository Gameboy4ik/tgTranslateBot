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
different_lang = types.KeyboardButton('...')
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
eng_next_btn1 = types.InlineKeyboardButton('next', callback_data='eng_next')
eng_different_lang_buttons1.add(
    languages_keyboard.list_eng_buttons[0],
    languages_keyboard.list_eng_buttons[1],
    languages_keyboard.list_eng_buttons[2],
    languages_keyboard.list_eng_buttons[3],
    languages_keyboard.list_eng_buttons[4],
    languages_keyboard.list_eng_buttons[5],
    languages_keyboard.list_eng_buttons[6],
    languages_keyboard.list_eng_buttons[7],
    languages_keyboard.list_eng_buttons[8],
    languages_keyboard.list_eng_buttons[9],
    languages_keyboard.list_eng_buttons[10],
    languages_keyboard.list_eng_buttons[11],
    languages_keyboard.list_eng_buttons[12],
    languages_keyboard.list_eng_buttons[13],
    languages_keyboard.list_eng_buttons[14],
    languages_keyboard.list_eng_buttons[15],
    languages_keyboard.list_eng_buttons[16],
    languages_keyboard.list_eng_buttons[17],
    languages_keyboard.list_eng_buttons[18],
    languages_keyboard.list_eng_buttons[19],
    languages_keyboard.list_eng_buttons[20],
    languages_keyboard.list_eng_buttons[21],
    languages_keyboard.list_eng_buttons[22],
    languages_keyboard.list_eng_buttons[23],
    languages_keyboard.list_eng_buttons[24],
    languages_keyboard.list_eng_buttons[25],
    languages_keyboard.list_eng_buttons[26],
    languages_keyboard.list_eng_buttons[27],
    languages_keyboard.list_eng_buttons[28],
    languages_keyboard.list_eng_buttons[29],
    languages_keyboard.list_eng_buttons[30],
    eng_next_btn1
)

eng_different_lang_buttons2 = types.InlineKeyboardMarkup(row_width=3)
eng_next_btn2 = types.InlineKeyboardButton('next', callback_data='eng_next2')
eng_back_btn = types.InlineKeyboardButton('back', callback_data='eng_back')
eng_different_lang_buttons2.add(
    languages_keyboard.list_eng_buttons[31],
    languages_keyboard.list_eng_buttons[32],
    languages_keyboard.list_eng_buttons[33],
    languages_keyboard.list_eng_buttons[34],
    languages_keyboard.list_eng_buttons[35],
    languages_keyboard.list_eng_buttons[36],
    languages_keyboard.list_eng_buttons[37],
    languages_keyboard.list_eng_buttons[38],
    languages_keyboard.list_eng_buttons[39],
    languages_keyboard.list_eng_buttons[40],
    languages_keyboard.list_eng_buttons[41],
    languages_keyboard.list_eng_buttons[42],
    languages_keyboard.list_eng_buttons[43],
    languages_keyboard.list_eng_buttons[44],
    languages_keyboard.list_eng_buttons[45],
    languages_keyboard.list_eng_buttons[46],
    languages_keyboard.list_eng_buttons[47],
    languages_keyboard.list_eng_buttons[48],
    languages_keyboard.list_eng_buttons[49],
    languages_keyboard.list_eng_buttons[50],
    languages_keyboard.list_eng_buttons[51],
    languages_keyboard.list_eng_buttons[52],
    languages_keyboard.list_eng_buttons[53],
    languages_keyboard.list_eng_buttons[54],
    languages_keyboard.list_eng_buttons[55],
    languages_keyboard.list_eng_buttons[56],
    languages_keyboard.list_eng_buttons[57],
    languages_keyboard.list_eng_buttons[58],
    languages_keyboard.list_eng_buttons[59],
    languages_keyboard.list_eng_buttons[60],
    eng_back_btn,
    eng_next_btn2
)

eng_different_lang_buttons3 = types.InlineKeyboardMarkup(row_width=3)
eng_next_btn3 = types.InlineKeyboardButton('next', callback_data='eng_next3')
eng_back_btn2 = types.InlineKeyboardButton('back', callback_data='eng_back2')
eng_different_lang_buttons3.add(
    languages_keyboard.list_eng_buttons[61],
    languages_keyboard.list_eng_buttons[62],
    languages_keyboard.list_eng_buttons[63],
    languages_keyboard.list_eng_buttons[64],
    languages_keyboard.list_eng_buttons[65],
    languages_keyboard.list_eng_buttons[66],
    languages_keyboard.list_eng_buttons[67],
    languages_keyboard.list_eng_buttons[68],
    languages_keyboard.list_eng_buttons[69],
    languages_keyboard.list_eng_buttons[70],
    languages_keyboard.list_eng_buttons[71],
    languages_keyboard.list_eng_buttons[72],
    languages_keyboard.list_eng_buttons[73],
    languages_keyboard.list_eng_buttons[74],
    languages_keyboard.list_eng_buttons[75],
    languages_keyboard.list_eng_buttons[76],
    languages_keyboard.list_eng_buttons[77],
    languages_keyboard.list_eng_buttons[78],
    languages_keyboard.list_eng_buttons[79],
    languages_keyboard.list_eng_buttons[80],
    languages_keyboard.list_eng_buttons[81],
    languages_keyboard.list_eng_buttons[82],
    languages_keyboard.list_eng_buttons[83],
    languages_keyboard.list_eng_buttons[84],
    languages_keyboard.list_eng_buttons[85],
    languages_keyboard.list_eng_buttons[86],
    languages_keyboard.list_eng_buttons[87],
    languages_keyboard.list_eng_buttons[88],
    languages_keyboard.list_eng_buttons[89],
    languages_keyboard.list_eng_buttons[90],
    eng_back_btn2,
    eng_next_btn3
)

eng_different_lang_buttons4 = types.InlineKeyboardMarkup(row_width=3)
eng_back_btn3 = types.InlineKeyboardButton('back', callback_data='eng_back3')
eng_different_lang_buttons4.add(
    languages_keyboard.list_eng_buttons[91],
    languages_keyboard.list_eng_buttons[92],
    languages_keyboard.list_eng_buttons[93],
    languages_keyboard.list_eng_buttons[94],
    languages_keyboard.list_eng_buttons[95],
    languages_keyboard.list_eng_buttons[96],
    languages_keyboard.list_eng_buttons[97],
    languages_keyboard.list_eng_buttons[98],
    languages_keyboard.list_eng_buttons[99],
    languages_keyboard.list_eng_buttons[100],
    languages_keyboard.list_eng_buttons[101],
    languages_keyboard.list_eng_buttons[102],
    languages_keyboard.list_eng_buttons[103],
    languages_keyboard.list_eng_buttons[104],
    languages_keyboard.list_eng_buttons[105],
    eng_back_btn3,
    languages_keyboard.list_eng_buttons[106]
)

rus_different_lang_buttons1 = types.InlineKeyboardMarkup(row_width=3)
rus_next_btn1 = types.InlineKeyboardButton('далее', callback_data='rus_next')
rus_different_lang_buttons1.add(
    languages_keyboard.list_rus_buttons[0],
    languages_keyboard.list_rus_buttons[1],
    languages_keyboard.list_rus_buttons[2],
    languages_keyboard.list_rus_buttons[3],
    languages_keyboard.list_rus_buttons[4],
    languages_keyboard.list_rus_buttons[5],
    languages_keyboard.list_rus_buttons[6],
    languages_keyboard.list_rus_buttons[7],
    languages_keyboard.list_rus_buttons[8],
    languages_keyboard.list_rus_buttons[9],
    languages_keyboard.list_rus_buttons[10],
    languages_keyboard.list_rus_buttons[11],
    languages_keyboard.list_rus_buttons[12],
    languages_keyboard.list_rus_buttons[13],
    languages_keyboard.list_rus_buttons[14],
    languages_keyboard.list_rus_buttons[15],
    languages_keyboard.list_rus_buttons[16],
    languages_keyboard.list_rus_buttons[17],
    languages_keyboard.list_rus_buttons[18],
    languages_keyboard.list_rus_buttons[19],
    languages_keyboard.list_rus_buttons[20],
    languages_keyboard.list_rus_buttons[21],
    languages_keyboard.list_rus_buttons[22],
    languages_keyboard.list_rus_buttons[23],
    languages_keyboard.list_rus_buttons[24],
    languages_keyboard.list_rus_buttons[25],
    languages_keyboard.list_rus_buttons[26],
    languages_keyboard.list_rus_buttons[27],
    languages_keyboard.list_rus_buttons[28],
    languages_keyboard.list_rus_buttons[29],
    languages_keyboard.list_rus_buttons[30],
    rus_next_btn1
)

rus_different_lang_buttons2 = types.InlineKeyboardMarkup(row_width=3)
rus_next_btn2 = types.InlineKeyboardButton('далее', callback_data='rus_next2')
rus_back_btn = types.InlineKeyboardButton('назад', callback_data='rus_back')
rus_different_lang_buttons2.add(
    languages_keyboard.list_rus_buttons[31],
    languages_keyboard.list_rus_buttons[32],
    languages_keyboard.list_rus_buttons[33],
    languages_keyboard.list_rus_buttons[34],
    languages_keyboard.list_rus_buttons[35],
    languages_keyboard.list_rus_buttons[36],
    languages_keyboard.list_rus_buttons[37],
    languages_keyboard.list_rus_buttons[38],
    languages_keyboard.list_rus_buttons[39],
    languages_keyboard.list_rus_buttons[40],
    languages_keyboard.list_rus_buttons[41],
    languages_keyboard.list_rus_buttons[42],
    languages_keyboard.list_rus_buttons[43],
    languages_keyboard.list_rus_buttons[44],
    languages_keyboard.list_rus_buttons[45],
    languages_keyboard.list_rus_buttons[46],
    languages_keyboard.list_rus_buttons[47],
    languages_keyboard.list_rus_buttons[48],
    languages_keyboard.list_rus_buttons[49],
    languages_keyboard.list_rus_buttons[50],
    languages_keyboard.list_rus_buttons[51],
    languages_keyboard.list_rus_buttons[52],
    languages_keyboard.list_rus_buttons[53],
    languages_keyboard.list_rus_buttons[54],
    languages_keyboard.list_rus_buttons[55],
    languages_keyboard.list_rus_buttons[56],
    languages_keyboard.list_rus_buttons[57],
    languages_keyboard.list_rus_buttons[58],
    languages_keyboard.list_rus_buttons[59],
    languages_keyboard.list_rus_buttons[60],
    rus_back_btn,
    rus_next_btn2
)

rus_different_lang_buttons3 = types.InlineKeyboardMarkup(row_width=3)
rus_next_btn3 = types.InlineKeyboardButton('далее', callback_data='rus_next3')
rus_back_btn2 = types.InlineKeyboardButton('назад', callback_data='rus_back2')
rus_different_lang_buttons3.add(
    languages_keyboard.list_rus_buttons[61],
    languages_keyboard.list_rus_buttons[62],
    languages_keyboard.list_rus_buttons[63],
    languages_keyboard.list_rus_buttons[64],
    languages_keyboard.list_rus_buttons[65],
    languages_keyboard.list_rus_buttons[66],
    languages_keyboard.list_rus_buttons[67],
    languages_keyboard.list_rus_buttons[68],
    languages_keyboard.list_rus_buttons[69],
    languages_keyboard.list_rus_buttons[70],
    languages_keyboard.list_rus_buttons[71],
    languages_keyboard.list_rus_buttons[72],
    languages_keyboard.list_rus_buttons[73],
    languages_keyboard.list_rus_buttons[74],
    languages_keyboard.list_rus_buttons[75],
    languages_keyboard.list_rus_buttons[76],
    languages_keyboard.list_rus_buttons[77],
    languages_keyboard.list_rus_buttons[78],
    languages_keyboard.list_rus_buttons[79],
    languages_keyboard.list_rus_buttons[80],
    languages_keyboard.list_rus_buttons[81],
    languages_keyboard.list_rus_buttons[82],
    languages_keyboard.list_rus_buttons[83],
    languages_keyboard.list_rus_buttons[84],
    languages_keyboard.list_rus_buttons[85],
    languages_keyboard.list_rus_buttons[86],
    languages_keyboard.list_rus_buttons[87],
    languages_keyboard.list_rus_buttons[88],
    languages_keyboard.list_rus_buttons[89],
    languages_keyboard.list_rus_buttons[90],
    rus_back_btn2,
    rus_next_btn3
)

rus_different_lang_buttons4 = types.InlineKeyboardMarkup(row_width=3)
rus_back_btn3 = types.InlineKeyboardButton('назад', callback_data='rus_back3')
rus_different_lang_buttons4.add(
    languages_keyboard.list_rus_buttons[91],
    languages_keyboard.list_rus_buttons[92],
    languages_keyboard.list_rus_buttons[93],
    languages_keyboard.list_rus_buttons[94],
    languages_keyboard.list_rus_buttons[95],
    languages_keyboard.list_rus_buttons[96],
    languages_keyboard.list_rus_buttons[97],
    languages_keyboard.list_rus_buttons[98],
    languages_keyboard.list_rus_buttons[99],
    languages_keyboard.list_rus_buttons[100],
    languages_keyboard.list_rus_buttons[101],
    languages_keyboard.list_rus_buttons[102],
    languages_keyboard.list_rus_buttons[103],
    languages_keyboard.list_rus_buttons[104],
    languages_keyboard.list_rus_buttons[105],
    rus_back_btn3,
    languages_keyboard.list_rus_buttons[106]
)

ukr_different_lang_buttons1 = types.InlineKeyboardMarkup(row_width=3)
ukr_next_btn1 = types.InlineKeyboardButton('далі', callback_data='ukr_next')
ukr_different_lang_buttons1.add(
    languages_keyboard.list_ukr_buttons[0],
    languages_keyboard.list_ukr_buttons[1],
    languages_keyboard.list_ukr_buttons[2],
    languages_keyboard.list_ukr_buttons[3],
    languages_keyboard.list_ukr_buttons[4],
    languages_keyboard.list_ukr_buttons[5],
    languages_keyboard.list_ukr_buttons[6],
    languages_keyboard.list_ukr_buttons[7],
    languages_keyboard.list_ukr_buttons[8],
    languages_keyboard.list_ukr_buttons[9],
    languages_keyboard.list_ukr_buttons[10],
    languages_keyboard.list_ukr_buttons[11],
    languages_keyboard.list_ukr_buttons[12],
    languages_keyboard.list_ukr_buttons[13],
    languages_keyboard.list_ukr_buttons[14],
    languages_keyboard.list_ukr_buttons[15],
    languages_keyboard.list_ukr_buttons[16],
    languages_keyboard.list_ukr_buttons[17],
    languages_keyboard.list_ukr_buttons[18],
    languages_keyboard.list_ukr_buttons[19],
    languages_keyboard.list_ukr_buttons[20],
    languages_keyboard.list_ukr_buttons[21],
    languages_keyboard.list_ukr_buttons[22],
    languages_keyboard.list_ukr_buttons[23],
    languages_keyboard.list_ukr_buttons[24],
    languages_keyboard.list_ukr_buttons[25],
    languages_keyboard.list_ukr_buttons[26],
    languages_keyboard.list_ukr_buttons[27],
    languages_keyboard.list_ukr_buttons[28],
    languages_keyboard.list_ukr_buttons[29],
    languages_keyboard.list_ukr_buttons[30],
    ukr_next_btn1
)

ukr_different_lang_buttons2 = types.InlineKeyboardMarkup(row_width=3)
ukr_next_btn2 = types.InlineKeyboardButton('далі', callback_data='ukr_next2')
ukr_back_btn = types.InlineKeyboardButton('назад', callback_data='ukr_back')
ukr_different_lang_buttons2.add(
    languages_keyboard.list_ukr_buttons[31],
    languages_keyboard.list_ukr_buttons[32],
    languages_keyboard.list_ukr_buttons[33],
    languages_keyboard.list_ukr_buttons[34],
    languages_keyboard.list_ukr_buttons[35],
    languages_keyboard.list_ukr_buttons[36],
    languages_keyboard.list_ukr_buttons[37],
    languages_keyboard.list_ukr_buttons[38],
    languages_keyboard.list_ukr_buttons[39],
    languages_keyboard.list_ukr_buttons[40],
    languages_keyboard.list_ukr_buttons[41],
    languages_keyboard.list_ukr_buttons[42],
    languages_keyboard.list_ukr_buttons[43],
    languages_keyboard.list_ukr_buttons[44],
    languages_keyboard.list_ukr_buttons[45],
    languages_keyboard.list_ukr_buttons[46],
    languages_keyboard.list_ukr_buttons[47],
    languages_keyboard.list_ukr_buttons[48],
    languages_keyboard.list_ukr_buttons[49],
    languages_keyboard.list_ukr_buttons[50],
    languages_keyboard.list_ukr_buttons[51],
    languages_keyboard.list_ukr_buttons[52],
    languages_keyboard.list_ukr_buttons[53],
    languages_keyboard.list_ukr_buttons[54],
    languages_keyboard.list_ukr_buttons[55],
    languages_keyboard.list_ukr_buttons[56],
    languages_keyboard.list_ukr_buttons[57],
    languages_keyboard.list_ukr_buttons[58],
    languages_keyboard.list_ukr_buttons[59],
    languages_keyboard.list_ukr_buttons[60],
    ukr_back_btn,
    ukr_next_btn2
)

ukr_different_lang_buttons3 = types.InlineKeyboardMarkup(row_width=3)
ukr_next_btn3 = types.InlineKeyboardButton('далі', callback_data='ukr_next3')
ukr_back_btn2 = types.InlineKeyboardButton('назад', callback_data='ukr_back2')
ukr_different_lang_buttons3.add(
    languages_keyboard.list_ukr_buttons[61],
    languages_keyboard.list_ukr_buttons[62],
    languages_keyboard.list_ukr_buttons[63],
    languages_keyboard.list_ukr_buttons[64],
    languages_keyboard.list_ukr_buttons[65],
    languages_keyboard.list_ukr_buttons[66],
    languages_keyboard.list_ukr_buttons[67],
    languages_keyboard.list_ukr_buttons[68],
    languages_keyboard.list_ukr_buttons[69],
    languages_keyboard.list_ukr_buttons[70],
    languages_keyboard.list_ukr_buttons[71],
    languages_keyboard.list_ukr_buttons[72],
    languages_keyboard.list_ukr_buttons[73],
    languages_keyboard.list_ukr_buttons[74],
    languages_keyboard.list_ukr_buttons[75],
    languages_keyboard.list_ukr_buttons[76],
    languages_keyboard.list_ukr_buttons[77],
    languages_keyboard.list_ukr_buttons[78],
    languages_keyboard.list_ukr_buttons[79],
    languages_keyboard.list_ukr_buttons[80],
    languages_keyboard.list_ukr_buttons[81],
    languages_keyboard.list_ukr_buttons[82],
    languages_keyboard.list_ukr_buttons[83],
    languages_keyboard.list_ukr_buttons[84],
    languages_keyboard.list_ukr_buttons[85],
    languages_keyboard.list_ukr_buttons[86],
    languages_keyboard.list_ukr_buttons[87],
    languages_keyboard.list_ukr_buttons[88],
    languages_keyboard.list_ukr_buttons[89],
    languages_keyboard.list_ukr_buttons[90],
    ukr_back_btn2,
    ukr_next_btn3
)

ukr_different_lang_buttons4 = types.InlineKeyboardMarkup(row_width=3)
ukr_back_btn3 = types.InlineKeyboardButton('назад', callback_data='ukr_back3')
ukr_different_lang_buttons4.add(
    languages_keyboard.list_ukr_buttons[91],
    languages_keyboard.list_ukr_buttons[92],
    languages_keyboard.list_ukr_buttons[93],
    languages_keyboard.list_ukr_buttons[94],
    languages_keyboard.list_ukr_buttons[95],
    languages_keyboard.list_ukr_buttons[96],
    languages_keyboard.list_ukr_buttons[97],
    languages_keyboard.list_ukr_buttons[98],
    languages_keyboard.list_ukr_buttons[99],
    languages_keyboard.list_ukr_buttons[100],
    languages_keyboard.list_ukr_buttons[101],
    languages_keyboard.list_ukr_buttons[102],
    languages_keyboard.list_ukr_buttons[103],
    languages_keyboard.list_ukr_buttons[104],
    languages_keyboard.list_ukr_buttons[105],
    ukr_back_btn3,
    languages_keyboard.list_ukr_buttons[106]
)
