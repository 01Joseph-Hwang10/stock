from stock_tracker.src.stock_tracker.notifier.main import notify_all
from shared.hooks.use_config import use_config
from shared.utils.time import now

def notify():
    config = use_config()
    if not bool(config):
        return
    if now().hour < 9:
        return
    if now().hour == 15 and now().minute > 30:
        return
    if now().hour > 15:
        return
    print('Executing Notification Job')
    notify_all()
