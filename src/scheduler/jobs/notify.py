from src.stock_tracker.notifier.main import notify_all
from datetime import datetime

def notify():
    now = datetime.now()
    if now.hour < 9:
        return
    if now.hour == 15 and now.minute > 30:
        return
    if now.hour > 15:
        return
    notify_all()
