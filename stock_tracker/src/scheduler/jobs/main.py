import atexit
from stock_tracker.src.scheduler.main import scheduler
from stock_tracker.src.scheduler.jobs.notify import notify

def start_jobs():
    notify_job = scheduler.add_job(notify, 'interval', minutes=5)

    atexit.register(lambda: notify_job.remove())
