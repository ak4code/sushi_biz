from django.conf import settings
import telebot
import vk
import uuid

session = vk.Session(access_token=settings.VK_BOT_TOKEN)
api = vk.API(session, v='5.92', lang='ru', )
ADMINS = settings.VK_ADMINS_IDS


def get_random_id():
    return uuid.uuid4().int


def vk_send_order(message):
    if settings.DEBUG:
        api.messages.send(user_ids='314252417', random_id=get_random_id(), message=message)
    else:
        api.messages.send(user_ids=ADMINS, random_id=get_random_id(), message=message)


tg_bot = telebot.TeleBot(settings.TG_BOT_TOKEN)


def tg_send_order(message):
    if settings.DEBUG:
        tg_bot.send_message(215750267, message)
    else:
        tg_bot.send_message(897458587, message)
        tg_bot.send_message(945903981, message)


def check_new_updates():
    updates = tg_bot.get_updates()
    for update in updates:
        print(update)
