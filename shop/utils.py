from django.template.loader import render_to_string
from .bots import tg_send_order


def order_create_notification(order):
    message = render_to_string('shop/order_notification_message.txt', {'order': order})
    try:
        tg_send_order(message)
    except:
        pass