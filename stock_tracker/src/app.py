import os
from flask import Flask
from stock_tracker.src.db.main import init_db
from stock_tracker.src.scheduler.jobs.main import start_jobs
from stock_tracker.src.routes.main import bp as main
from stock_tracker.src.routes.config import bp as config

def init_app():
    app = Flask(__name__)

    init_db(app)
    start_jobs()

    app.register_blueprint(main)
    app.register_blueprint(config)

    if os.environ.get('DEBUG') == 'True':
        app.debug = True
    else:
        app.debug = False
    return app

def init_app_dev():
    import scripts.set_dev_env
    return init_app()
