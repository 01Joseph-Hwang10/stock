import os
from flask import Flask
from scripts.set_dev_env import load_env
from stock_tracker.src.db.main import init_db
from stock_tracker.src.routes.main import bp as main
from stock_tracker.src.routes.config import bp as config
from stock_tracker.src.scheduler.main import init_scheduler

def init_app():
    app = Flask(__name__)

    init_db(app)
    init_scheduler()

    app.register_blueprint(main)
    app.register_blueprint(config)

    if os.environ.get('DEBUG') == 'True':
        app.debug = True
    else:
        app.debug = False
    return app

def init_app_dev():
    load_env()
    return init_app()
