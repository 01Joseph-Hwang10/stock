from datetime import datetime
from stock_tracker.src.stock_tracker.notifier.main import notify_all
from shared.hooks.use_config import use_config

def notify():
    config = use_config()
    print(f'Notify all users')
    if not bool(config):
        return
    now = datetime.now()
    if now.hour < 9:
        return
    if now.hour == 15 and now.minute > 30:
        return
    if now.hour > 15:
        return
    print(f'Executing Notification Job')
    notify_all()
