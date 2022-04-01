from telebot import telebot, types, custom_filters
from languages import *
from cities import Cities
from dotenv import load_dotenv
import os

data = Cities()

load_dotenv('.env')
TOKEN = os.getenv("SECRET_TOKEN")
bot = telebot.TeleBot(TOKEN)

# --------------Import Messages (4 languages)-------------
languages_available = {
    "English": EnglishMessages(),
    "Italiano": ItaMessages(),
    "Українська": UkrMessages(),
    "Русский": RusMessages()
}
lang_list = list(languages_available.keys())
lang = languages_available["English"]



def set_option_menu(user_data, message_id, text):
    """Sets one/multiple keyboard items menu and sends message"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for n in user_data:
        item = types.KeyboardButton(n)
        markup.add(item)
    bot.send_message(message_id, text, parse_mode='html', reply_markup=markup)


# -----------------Greetings and Choosing Language--------------
@bot.message_handler(commands=['start'])
def start(message):
    set_option_menu(languages_available, message.chat.id, lang.select_language)


# ----------------------Set Main Menu----------------
@bot.message_handler(text=lang_list)
def main_manu_message(message):
    global lang
    lang = languages_available[message.text]

    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(lang.option_center, callback_data=lang.callback_center)
    item2 = types.InlineKeyboardButton(lang.option_aid, callback_data=lang.callback_aid)
    markup.add(item, item2)
    bot.send_message(message.chat.id, lang.greeting, parse_mode='html', reply_markup=markup)


# ---------------Show Volunteer Centers Addresses--------------
@bot.message_handler(text=data.list)
def view_address_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(lang.option_aid, callback_data=lang.callback_aid)
    markup.add(item)
    bot.send_message(message.chat.id, data.cities[message.text], parse_mode='html', reply_markup=markup)


# ------------Show List of cities with Centers/ Aid needed--------------
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == lang.callback_center:
                set_option_menu(data.cities, call.message.chat.id, lang.select_city)
            elif call.data == lang.callback_aid:
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton(lang.option_center, callback_data=lang.callback_center)
                markup.add(item)
                bot.send_message(call.message.chat.id, lang.aid_list, parse_mode='html', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, lang.error)
        print(repr(e))


bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.polling(none_stop=True)





