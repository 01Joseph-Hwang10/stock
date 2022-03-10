from flask import Flask
from apps.shared.hooks.use_config import use_config, Config
from apps.webhook.src.routes.main import main

app = Flask(__name__)
app.register_blueprint(main)

config: Config = use_config()

app.run(debug=config['env']['debug'])
