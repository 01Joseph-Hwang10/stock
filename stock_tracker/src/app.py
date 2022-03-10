from flask import Flask
from stock_tracker.src.hooks.use_config import use_config
from stock_tracker.src.db.main import init_db
from stock_tracker.src.scheduler.jobs.main import start_jobs
from stock_tracker.src.routes.main import bp as main
from stock_tracker.src.routes.config import bp as config
from stock_tracker.src.utils.null_safety import as_bool

app = Flask(__name__)

init_db(app)
start_jobs()

app.register_blueprint(main)
app.register_blueprint(config)

config = use_config(app)
app.debug = config['env']['debug'] if as_bool(config) else False
