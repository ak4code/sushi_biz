from django.conf import settings
import telebot

TG_GROUP = settings.TG_GROUP
tg_bot = telebot.TeleBot(settings.TG_BOT_TOKEN)


def tg_send_order(message):
    tg_bot.send_message(TG_GROUP, message)


def check_new_updates():
    updates = tg_bot.get_updates()
    for update in updates:
        print(update)
