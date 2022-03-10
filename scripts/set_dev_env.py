import os
from scripts.helpers.env_to_dict import use_env

def load_env():
    env = use_env()

    os.environ.setdefault('DEBUG', str(env.debug))
    os.environ.setdefault('SECRET_KEY', env.secret_key)
