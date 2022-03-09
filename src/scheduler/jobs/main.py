import atexit
from src.scheduler.main import scheduler
from src.scheduler.jobs.notify import notify

def start_jobs():
    notify_job = scheduler.add_job(notify, 'interval', minutes=5)

    atexit.register(lambda: notify_job.remove())
