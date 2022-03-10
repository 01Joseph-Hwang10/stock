import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job
from stock_tracker.src.scheduler.jobs.notify import notify
from stock_tracker.src.scheduler.config import jobstores, executors, job_defaults

class Scheduler:

    notify_job: Job

    def __init__(self):
        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

    def init(self):
        # Register Jobs
        self.notify_job = self.scheduler.add_job(notify, 'interval', minutes=5)
        atexit.register(lambda: self.notify_job.remove())
        
        # Start Scheduler
        self.scheduler.start()
        print("Scheduler started")
    
    def get_job_status(self, job: Job) -> str:
        print(job)
        if not bool(job):
            return 'Not Initialized'
        if bool(job.next_run_time):
            return 'Running'
        return 'Not Running'

    def status_of(self, job_name: str) -> str:
        if job_name == 'notify':
            return self.get_job_status(self.notify_job)
        return 'Job Not Found'

scheduler = Scheduler()
