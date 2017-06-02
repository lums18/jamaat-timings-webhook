#!/usr/bin/env python3.6

import telegram
from flask import Flask, request

chinkubot=os.environ['chinkubot']
TOKEN=chinkubot
HOOK=chinkubot
URL='abnaeem0.pythonanywhere.com/'

global bot
bot = telegram.Bot(token=TOKEN)

def is_new_user(chat_id):
    return True

app = Flask(__name__)

@app.route('/'+HOOK, methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True),bot)

        chat_id = update.message.chat.id
        if is_new_user(chat_id):
            bot.sendMessage(chat_id=chat_id,text='Searching for Masjids')

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text  ##.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'
    ##https://github.com/sooyhwang/Simple-Echo-Telegram-Bot


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://'+URL+'/'+HOOK)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'
