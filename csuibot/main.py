import flask
import telebot
import logging
from .utils.zodiac import lookup_zodiac, lookup_chinese_zodiac

app = flask.Flask(__name__)
app.config.from_object('csuibot.config')
logger = telebot.logger
logger.setLevel(logging.INFO)

bot = telebot.TeleBot(app.config['TELEGRAM_BOT_TOKEN'], threaded=False)

webhook_url_base = app.config['WEBHOOK_HOST']


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am ZoShio bot.\n"
                  "Please insert a command with a date and I'll find out his/her "
                  "zodiac or shio. Example: /zodiac yyyy-mm-dd"))


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)


@bot.message_handler(regexp=r'^/zodiac \d{4}\-\d{2}\-\d{2}$')
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))

    try:
        zodiac = lookup_zodiac(month, day)
    except ValueError:
        bot.reply_to(message, 'Month or day is invalid')
    else:
        bot.reply_to(message, zodiac)


@bot.message_handler(regexp=r'^/shio \d{4}\-\d{2}\-\d{2}$')
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = parse_date(date_str)
    app.logger.debug('year = {}'.format(year))

    try:
        zodiac = lookup_chinese_zodiac(year)
    except ValueError:
        bot.reply_to(message, 'Year is invalid')
    else:
        bot.reply_to(message, zodiac)


def parse_date(text):
    return tuple(map(int, text.split('-')))


@app.route("/bot", methods=['POST'])
def get_message():
    if flask.request.headers.get('content-type') == 'application/json':
        bot.process_new_updates([telebot.types.Update.de_json
                                (flask.request.get_data().decode("utf-8"))])
        return "!", 200
    else:
        flask.abort(403)


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url_base)

    return "Bot is Running", 200

# Test for local server
# bot.remove_webhook()
# bot.polling()
