import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from stock_tracker.src.scheduler.jobs.notify import notify

jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

def init_scheduler():
    notify_job = scheduler.add_job(notify, 'interval', minutes=5)
    atexit.register(lambda: notify_job.remove())
    scheduler.start()
    print("Scheduler started")
