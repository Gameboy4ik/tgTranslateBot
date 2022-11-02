from telebot import types

TOKEN = '5752873117:AAE06L9-W9wy-OOiyjeWrOOknbf4Wte21pY' # bot token

ENG_LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

RUS_LANGUAGES = {
    'af': 'африканский',
    'sq': 'албанский',
    'am': 'амхарский',
    'ar': 'арабский',
    'hy': 'армянский',
    'az': 'азербайджанский',
    'eu': 'баскский',
    'be': 'белорусский',
    'bn': 'бенгальский',
    'bs': 'боснийский',
    'bg': 'болгарский',
    'ca': 'каталонский',
    'ceb': 'кебуано',
    'ny': 'чичева',
    'zh-cn': 'китайский (упрощенный)',
    'zh-tw': 'китайский (традиционный)',
    'co': 'корсиканский',
    'hr': 'хорватский',
    'cs': 'чешский',
    'da': 'датский',
    'nl': 'голландский',
    'en': 'английский',
    'eo': 'эсперанто',
    'et': 'эстонский',
    'tl': 'филиппинский',
    'fi': 'финский',
    'fr': 'французский',
    'fy': 'фризский',
    'gl': 'галицкий',
    'ka': 'грузинский',
    'de': 'немецкий',
    'el': 'греческий',
    'gu': 'гуджарати',
    'ht': 'гаитянский креольский',
    'ha': 'хауса',
    'haw': 'гавайский',
    'iw': 'иврит',
    'he': 'иврит',
    'hi': 'хинди',
    'hmn': 'хмонг',
    'hu': 'венгерский',
    'is': 'исландский',
    'ig': 'игбо',
    'id': 'индонезийский',
    'ga': 'ирландский',
    'it': 'итальянский',
    'ja': 'японский',
    'jw': 'яванский',
    'kn': 'каннадский',
    'kk': 'казахский',
    'km': 'кхмерский',
    'ko': 'корейский',
    'ku': 'курдский (курманджи)',
    'ky': 'кыргызский',
    'lo': 'лаосский',
    'la': 'латинский',
    'lv': 'латышский',
    'lt': 'литовский',
    'lb': 'люксембургский',
    'mk': 'македонский',
    'mg': 'малагасийский',
    'ms': 'малайский',
    'ml': 'малаялам',
    'mt': 'мальтийский',
    'mi': 'маори',
    'mr': 'маратхи',
    'mn': 'монгольский',
    'my': 'мьянма (бирманский)',
    'ne': 'непальский',
    'no': 'норвежский',
    'or': 'одиа',
    'ps': 'пушту',
    'fa': 'персидский',
    'pl': 'польский',
    'pt': 'португальский',
    'pa': 'панджаби',
    'ro': 'румынский',
    'ru': 'русский',
    'sm': 'самоанский',
    'gd': 'шотландский гэльский',
    'sr': 'сербский',
    'st': 'сесото',
    'sn': 'шона',
    'sd': 'синдхи',
    'si': 'сингальский',
    'sk': 'словацкий',
    'sl': 'словенский',
    'so': 'сомалийский',
    'es': 'испанский',
    'su': 'суданский',
    'sw': 'суахили',
    'sv': 'шведский',
    'tg': 'таджикский',
    'ta': 'тамильский',
    'te': 'телугу',
    'th': 'тайский',
    'tr': 'турецкий',
    'uk': 'украинский',
    'ur': 'урду',
    'ug': 'уйгурский',
    'uz': 'узбекский',
    'vi': 'вьетнамский',
    'cy': 'валлийский',
    'xh': 'коса',
    'yi': 'yiddish',
    'yo': 'йоруба',
    'zu': 'зулу',
}

UKR_LANGUAGES = {
    'af': 'африканська',
    'sq': 'албанська',
    'am': 'амхарська',
    'ar': 'арабська',
    'hy': 'вірменська',
    'az': 'азербайджанська',
    'eu': 'баскська',
    'be': 'білоруська',
    'bn': 'бенгальська',
    'bs': 'боснійська',
    'bg': 'болгарська',
    'ca': 'каталонська',
    'ceb': 'себуано',
    'ny': 'чева',
    'zh-cn': 'китайська (спрощена)',
    'zh-tw': 'китайська (традиційна)',
    'co': 'корсиканська',
    'hr': 'хорватська',
    'cs': 'чеська',
    'da': 'датська',
    'nl': 'голландська',
    'en': 'англійська',
    'eo': 'есперанто',
    'et': 'естонська',
    'tl': 'філіппінська',
    'fi': 'фінська',
    'fr': 'французька',
    'fy': 'фризька',
    'gl': 'галицька',
    'ka': 'грузинська',
    'de': 'німецька',
    'el': 'грецька',
    'gu': 'гуджараті',
    'ht': 'гаїтянський креольський',
    'ha': 'хауса',
    'haw': 'гавайський',
    'iw': 'іврит',
    'he': 'іврит',
    'hi': 'гінді',
    'hmn': 'хмонг',
    'hu': 'угорська',
    'is': 'ісландська',
    'ig': 'ігбо',
    'id': 'індонезійська',
    'ga': 'ірландська',
    'it': 'італійська',
    'ja': 'японська',
    'jw': 'яванська',
    'kn': 'каннадська',
    'kk': 'казахська',
    'km': 'кхмерська',
    'ko': 'корейська',
    'ku': 'курдська (курманджі)',
    'ky': 'киргизька',
    'lo': 'лаоська',
    'la': 'латинська',
    'lv': 'латиська',
    'lt': 'литовська',
    'lb': 'люксембурзька',
    'mk': 'македонська',
    'mg': 'малагасійська',
    'ms': 'малайська',
    'ml': 'малаялам',
    'mt': 'мальтійська',
    'mi': 'маорі',
    'mr': 'маратхі',
    'mn': 'монгольська',
    'my': "м'янма (бірманська)",
    'ne': 'непальська',
    'no': 'норвезька',
    'or': 'одія',
    'ps': 'пушту',
    'fa': 'перська',
    'pl': 'польська',
    'pt': 'португальська',
    'pa': 'панджабі',
    'ro': 'румунська',
    'ru': 'російська',
    'sm': 'самоанська',
    'gd': 'шотландська гельська',
    'sr': 'сербська',
    'st': 'сесото',
    'sn': 'шона',
    'sd': 'синдхі',
    'si': 'сингальська',
    'sk': 'словацька',
    'sl': 'словенська',
    'so': 'сомалійська',
    'es': 'іспанська',
    'su': 'суданська',
    'sw': 'суахілі',
    'sv': 'шведська',
    'tg': 'таджицька',
    'ta': 'тамільська',
    'te': 'телугу',
    'th': 'тайська',
    'tr': 'турецька',
    'uk': 'українська',
    'ur': 'урду',
    'ug': 'уйгурська',
    'uz': 'узбецька',
    'vi': "в'єтнамська",
    'cy': 'валлійська',
    'xh': 'коса',
    'yi': 'ідиш',
    'yo': 'йоруба',
    'zu': 'зулу',
}

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
start_markup.add(en_lang, ua_lang, ru_lang)

ukr_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
ukr_different_lang = types.KeyboardButton(ukrainian[6])
ukr_different_interface_lang = types.KeyboardButton(ukrainian[8])
ukr_menu.add(ukr_different_lang, ukr_different_interface_lang)

rus_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
rus_different_lang = types.KeyboardButton(russian[6])
rus_different_interface_lang = types.KeyboardButton(russian[8])
rus_menu.add(rus_different_lang, rus_different_interface_lang)

eng_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
eng_different_lang = types.KeyboardButton(english[6])
eng_different_interface_lang = types.KeyboardButton(english[8])
eng_menu.add(eng_different_lang, eng_different_interface_lang)