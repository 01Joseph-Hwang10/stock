from stock_tracker.src.stock_tracker.notifier.main import notify_all
from shared.hooks.use_config import use_config
from datetime import timezone, timedelta, datetime

KST = timezone(timedelta(hours=9))

def notify():
    config = use_config()
    if not bool(config):
        return
    now = datetime.now(KST)
    if now.hour < 9:
        return
    if now.hour == 15 and now.minute > 30:
        return
    if now.hour > 15:
        return
    print('Executing Notification Job')
    notify_all()
