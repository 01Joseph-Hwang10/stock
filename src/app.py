from flask import Flask
from src.db.main import init_db
from src.hooks.use_config import use_config, Config
from src.scheduler.jobs.main import start_jobs
from src.routes.main import main

app = Flask(__name__)

init_db(app)
start_jobs()

app.register_blueprint(main)

config: Config = use_config(app)
app.run(debug=config['env']['debug'])
