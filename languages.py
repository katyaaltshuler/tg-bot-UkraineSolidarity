class EnglishMessages:
    def __init__(self):
        self.select_language = '<b>Welcome to Ukrainian Solidarity Bot </b> 🇺🇦 \n\nOur bot was created to support the ' \
                               'Ukrainian people and assist Ukrainian diaspora in Italy 🇮🇹 \n\nHere you can find ' \
                               'information ' \
                               'about volunteer centers for the collection of humanitarian aid, necessary products, ' \
                               'as well as ' \
                               'refugee registration addresses in Italy.\n\n<b>Please, select your language: </b>'
        self.greeting = '<b>Select item that you need information for:</b>'
        self.option_center = 'The nearest volunteer center'
        self.callback_center = 'eng_centers'
        self.option_aid = 'What is collected urgently'
        self.callback_aid = 'eng_collection'
        self.select_city = 'Please, select your city:'
        self.error = "Sorry, I didn't catch, please select the desired item from list"
        self.aid_list = '<b>Cose serve quest\'ora:</b>\n\n❕ Coperte\n❕ Cuscini con riempimento sintetico\n❕ Tappetini ' \
                        'isolanti\n❕ Biancheria da letto' \
                        f'\n❕ Sacchi a pelo\n❕ Powerbank\n❕ Torce\n❕ Kit primo soccorso\n❕ Prodotti per bambini e adulti'


class UkrMessages:
    def __init__(self):
        self.select_language = '<b>Welcome to Ukrainian Solidarity Bot </b> 🇺🇦 \n\nOur bot was created to support the ' \
                               'Ukrainian people and assist Ukrainian diaspora in Italy 🇮🇹 \n\nHere you can find ' \
                               'information ' \
                               'about volunteer centers for the collection of humanitarian aid, necessary products, ' \
                               'as well as ' \
                               'refugee registration addresses in Italy.\n\n<b>Please, select your language: </b>'
        self.greeting = '<b> Вітаємо </b>🇺🇦 🇮🇹 \n\nНаш бот створений для підтримки українського народу та ' \
                        'допомоги українській ' \
                        'діаспорі в Італії. \n\nТут можна знайти інформацію про волонтерські центри для збору ' \
                        'гуманітарної ' \
                        'допомоги, необхідних продуктів, а також адреси реєстрації біженців в Італії.' \
                        '\n\n<b>Виберіть пункт, за яким вам потрібна інформація</b>'
        self.option_center = 'Знайдіть найближчий волонтерський центр'
        self.callback_center = 'ukr_centers'
        self.option_aid = 'Що збирають терміново'
        self.callback_aid= 'ukr_collection'
        self.select_city = 'Виберіть найближче місто:'
        self.error = "Вибачте, я вас не розумію, будь ласка, виберіть потрібний пункт зі списку"
        self.aid_list = '<b>Что требуется в данный момент:</b>\n\n❕ Одеяла/Пледы\n❕ Подушки с синтетическим ' \
                        'наполнением\n❕ Спальные мешки\n❕ Постельное белье' \
                        f'\n❕ Портативная зарядка\n❕ Фонарики\n❕ Набор для первой помощи\n❕ Продукты для детей'


class RusMessages:
    def __init__(self):
        self.select_language = '<b>Welcome to Ukrainian Solidarity Bot </b> 🇺🇦 \n\nOur bot was created to support ' \
                               'the ' \
                               'Ukrainian people and assist Ukrainian diaspora in Italy 🇮🇹 \n\nHere you can find ' \
                               'information ' \
                               'about volunteer centers for the collection of humanitarian aid, necessary products, ' \
                               'as well as ' \
                               'refugee registration addresses in Italy.\n\n<b>Please, select your language: </b>'
        self.greeting = '<b>Приветствуем </b>🇺🇦 🇮🇹 \n\nНаш бот создан для поддержки украинского народа и помощи ' \
                        'украинской ' \
                        'диаспоре в Италии. \n\nЗдесь можно найти информацию о волонтерских центрах для сбора ' \
                        'гуманитарной ' \
                        'помощи, необходимых продуктах, а также адреса регистрации беженцев в Италии.\n\n<b>Выберите ' \
                        'пункт, ' \
                        'по которому вам нужна информация: </b>'
        self.option_center = 'Ближайший волонтерский центр'
        self.callback_center = 'rus_centers'
        self.option_aid = 'Что собирается в срочном порядке'
        self.callback_aid = 'rus_collection'
        self.select_city = 'Выберите ваш город:'
        self.error = "Извините, я вас не понимаю, пожалуйста, выберите нужный пункт из списка"
        self.aid_list = '<b>Что требуется в данный момент:</b>\n\n❕ Одеяла/Пледы\n❕ Подушки с синтетическим наполнением' \
                        '\n❕ Спальные мешки\n❕ Постельное белье' \
                        f'\n❕ Портативная зарядка\n❕ Фонарики\n❕ Набор для первой помощи\n❕ Продукты для детей'


class ItaMessages:
    def __init__(self):
        self.select_language = '<b>Welcome to Ukrainian Solidarity Bot </b> 🇺🇦 \n\nOur bot was created to support the ' \
                               'Ukrainian people and assist Ukrainian diaspora in Italy 🇮🇹 \n\nHere you can find ' \
                               'information ' \
                               'about volunteer centers for the collection of humanitarian aid, necessary products, ' \
                               'as well as ' \
                               'refugee registration addresses in Italy.\n\n<b>Please, select your language: </b>'
        self.greeting = '<b>Buongiorno </b> 🇺🇦 🇮🇹 \n\nQui puoi trovare informazioni sui centri di volontariato per ' \
                        'la raccolta di aiuti umanitari, prodotti necessari e indirizzi di registrazione dei rifugiati ' \
                        'in Italia.\n\n<b>Seleziona l\'articolo per il quale hai bisogno di informazioni:</b>'
        self.option_center = 'Trova il centro di volontariato più vicino'
        self.callback_center = 'ita_centers'
        self.option_aid = 'Cosa viene raccolto urgentemente'
        self.callback_aid = 'ita_collection'
        self.select_city = 'Seleziona la tua città:'
        self.error = "Non ho capito, per favore seleziona l'elemento dall'elenco"
        self.aid_list = '<b>Cose serve quest\'ora:</b>\n\n❕ Coperte\n❕ Cuscini con riempimento sintetico\n❕ ' \
                        'Tappetini isolanti\n❕ Biancheria da letto' \
                        f'\n❕ Sacchi a pelo\n❕ Powerbank\n❕ Torce\n❕ Kit primo soccorso\n❕ Prodotti per bambini e adulti'
