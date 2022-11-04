from telebot import types

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

btn0 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[0], callback_data=list(ENG_LANGUAGES.keys())[0])
btn1 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[1], callback_data=list(ENG_LANGUAGES.keys())[1])
btn2 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[2], callback_data=list(ENG_LANGUAGES.keys())[2])
btn3 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[3], callback_data=list(ENG_LANGUAGES.keys())[3])
btn4 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[4], callback_data=list(ENG_LANGUAGES.keys())[4])
btn5 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[5], callback_data=list(ENG_LANGUAGES.keys())[5])
btn6 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[6], callback_data=list(ENG_LANGUAGES.keys())[6])
btn7 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[7], callback_data=list(ENG_LANGUAGES.keys())[7])
btn8 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[8], callback_data=list(ENG_LANGUAGES.keys())[8])
btn9 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[9], callback_data=list(ENG_LANGUAGES.keys())[9])
btn10 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[10], callback_data=list(ENG_LANGUAGES.keys())[10])
btn11 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[11], callback_data=list(ENG_LANGUAGES.keys())[11])
btn12 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[12], callback_data=list(ENG_LANGUAGES.keys())[12])
btn13 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[13], callback_data=list(ENG_LANGUAGES.keys())[13])
btn14 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[14], callback_data=list(ENG_LANGUAGES.keys())[14])
btn15 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[15], callback_data=list(ENG_LANGUAGES.keys())[15])
btn16 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[16], callback_data=list(ENG_LANGUAGES.keys())[16])
btn17 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[17], callback_data=list(ENG_LANGUAGES.keys())[17])
btn18 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[18], callback_data=list(ENG_LANGUAGES.keys())[18])
btn19 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[19], callback_data=list(ENG_LANGUAGES.keys())[19])
btn20 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[20], callback_data=list(ENG_LANGUAGES.keys())[20])
btn21 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[21], callback_data=list(ENG_LANGUAGES.keys())[21])
btn22 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[22], callback_data=list(ENG_LANGUAGES.keys())[22])
btn23 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[23], callback_data=list(ENG_LANGUAGES.keys())[23])
btn24 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[24], callback_data=list(ENG_LANGUAGES.keys())[24])
btn25 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[25], callback_data=list(ENG_LANGUAGES.keys())[25])
btn26 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[26], callback_data=list(ENG_LANGUAGES.keys())[26])
btn27 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[27], callback_data=list(ENG_LANGUAGES.keys())[27])
btn28 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[28], callback_data=list(ENG_LANGUAGES.keys())[28])
btn29 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[29], callback_data=list(ENG_LANGUAGES.keys())[29])
btn30 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[30], callback_data=list(ENG_LANGUAGES.keys())[30])
btn31 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[31], callback_data=list(ENG_LANGUAGES.keys())[31])
btn32 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[32], callback_data=list(ENG_LANGUAGES.keys())[32])
btn33 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[33], callback_data=list(ENG_LANGUAGES.keys())[33])
btn34 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[34], callback_data=list(ENG_LANGUAGES.keys())[34])
btn35 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[35], callback_data=list(ENG_LANGUAGES.keys())[35])
btn36 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[36], callback_data=list(ENG_LANGUAGES.keys())[36])
btn37 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[37], callback_data=list(ENG_LANGUAGES.keys())[37])
btn38 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[38], callback_data=list(ENG_LANGUAGES.keys())[38])
btn39 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[39], callback_data=list(ENG_LANGUAGES.keys())[39])
btn40 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[40], callback_data=list(ENG_LANGUAGES.keys())[40])
btn41 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[41], callback_data=list(ENG_LANGUAGES.keys())[41])
btn42 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[42], callback_data=list(ENG_LANGUAGES.keys())[42])
btn43 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[43], callback_data=list(ENG_LANGUAGES.keys())[43])
btn44 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[44], callback_data=list(ENG_LANGUAGES.keys())[44])
btn45 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[45], callback_data=list(ENG_LANGUAGES.keys())[45])
btn46 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[46], callback_data=list(ENG_LANGUAGES.keys())[46])
btn47 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[47], callback_data=list(ENG_LANGUAGES.keys())[47])
btn48 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[48], callback_data=list(ENG_LANGUAGES.keys())[48])
btn49 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[49], callback_data=list(ENG_LANGUAGES.keys())[49])
btn50 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[50], callback_data=list(ENG_LANGUAGES.keys())[50])
btn51 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[51], callback_data=list(ENG_LANGUAGES.keys())[51])
btn52 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[52], callback_data=list(ENG_LANGUAGES.keys())[52])
btn53 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[53], callback_data=list(ENG_LANGUAGES.keys())[53])
btn54 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[54], callback_data=list(ENG_LANGUAGES.keys())[54])
btn55 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[55], callback_data=list(ENG_LANGUAGES.keys())[55])
btn56 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[56], callback_data=list(ENG_LANGUAGES.keys())[56])
btn57 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[57], callback_data=list(ENG_LANGUAGES.keys())[57])
btn58 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[58], callback_data=list(ENG_LANGUAGES.keys())[58])
btn59 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[59], callback_data=list(ENG_LANGUAGES.keys())[59])
btn60 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[60], callback_data=list(ENG_LANGUAGES.keys())[60])
btn61 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[61], callback_data=list(ENG_LANGUAGES.keys())[61])
btn62 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[62], callback_data=list(ENG_LANGUAGES.keys())[62])
btn63 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[63], callback_data=list(ENG_LANGUAGES.keys())[63])
btn64 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[64], callback_data=list(ENG_LANGUAGES.keys())[64])
btn65 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[65], callback_data=list(ENG_LANGUAGES.keys())[65])
btn66 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[66], callback_data=list(ENG_LANGUAGES.keys())[66])
btn67 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[67], callback_data=list(ENG_LANGUAGES.keys())[67])
btn68 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[68], callback_data=list(ENG_LANGUAGES.keys())[68])
btn69 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[69], callback_data=list(ENG_LANGUAGES.keys())[69])
btn70 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[70], callback_data=list(ENG_LANGUAGES.keys())[70])
btn71 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[71], callback_data=list(ENG_LANGUAGES.keys())[71])
btn72 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[72], callback_data=list(ENG_LANGUAGES.keys())[72])
btn73 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[73], callback_data=list(ENG_LANGUAGES.keys())[73])
btn74 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[74], callback_data=list(ENG_LANGUAGES.keys())[74])
btn75 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[75], callback_data=list(ENG_LANGUAGES.keys())[75])
btn76 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[76], callback_data=list(ENG_LANGUAGES.keys())[76])
btn77 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[77], callback_data=list(ENG_LANGUAGES.keys())[77])
btn78 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[78], callback_data=list(ENG_LANGUAGES.keys())[78])
btn79 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[79], callback_data=list(ENG_LANGUAGES.keys())[79])
btn80 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[80], callback_data=list(ENG_LANGUAGES.keys())[80])
btn81 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[81], callback_data=list(ENG_LANGUAGES.keys())[81])
btn82 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[82], callback_data=list(ENG_LANGUAGES.keys())[82])
btn83 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[83], callback_data=list(ENG_LANGUAGES.keys())[83])
btn84 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[84], callback_data=list(ENG_LANGUAGES.keys())[84])
btn85 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[85], callback_data=list(ENG_LANGUAGES.keys())[85])
btn86 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[86], callback_data=list(ENG_LANGUAGES.keys())[86])
btn87 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[87], callback_data=list(ENG_LANGUAGES.keys())[87])
btn88 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[88], callback_data=list(ENG_LANGUAGES.keys())[88])
btn89 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[89], callback_data=list(ENG_LANGUAGES.keys())[89])
btn90 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[90], callback_data=list(ENG_LANGUAGES.keys())[90])
btn91 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[91], callback_data=list(ENG_LANGUAGES.keys())[91])
btn92 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[92], callback_data=list(ENG_LANGUAGES.keys())[92])
btn93 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[93], callback_data=list(ENG_LANGUAGES.keys())[93])
btn94 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[94], callback_data=list(ENG_LANGUAGES.keys())[94])
btn95 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[95], callback_data=list(ENG_LANGUAGES.keys())[95])
btn96 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[96], callback_data=list(ENG_LANGUAGES.keys())[96])
btn97 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[97], callback_data=list(ENG_LANGUAGES.keys())[97])
btn98 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[98], callback_data=list(ENG_LANGUAGES.keys())[98])
btn99 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[99], callback_data=list(ENG_LANGUAGES.keys())[99])
btn100 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[100], callback_data=list(ENG_LANGUAGES.keys())[100])
btn101 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[101], callback_data=list(ENG_LANGUAGES.keys())[101])
btn102 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[102], callback_data=list(ENG_LANGUAGES.keys())[102])
btn103 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[103], callback_data=list(ENG_LANGUAGES.keys())[103])
btn104 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[104], callback_data=list(ENG_LANGUAGES.keys())[104])
btn105 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[105], callback_data=list(ENG_LANGUAGES.keys())[105])
btn106 = types.InlineKeyboardButton(text=list(ENG_LANGUAGES.values())[106], callback_data=list(ENG_LANGUAGES.keys())[106])