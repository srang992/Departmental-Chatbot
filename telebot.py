from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from main_files.chat import *

with open("token.txt", "r") as f:
    lines = f.readlines()
    updater = Updater(lines[0])


def start(update: Update, context: CallbackContext):
    update.message.reply_text("""
    Hello! My name is Mike. if you want to know how can I do, just ask - How can you help me?
    """)


def main_response(update: Update, context: CallbackContext):
    answer = get_response(update.message.text, interpreter=interpreter, param_value_1=param_val1)
    update.message.reply_text(answer)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, main_response))

updater.start_polling()
