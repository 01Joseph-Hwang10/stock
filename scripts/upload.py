import requests
from subprocess import Popen
from http import HTTPStatus
from urllib.parse import urljoin
from shared.hooks.use_config import use_config
from shared.utils.constants import SERVER_URL
from scripts.helpers.env_to_dict import use_env

URL = urljoin(SERVER_URL, '/config/upload')

def upload_config():
    env = use_env()
    headers = {
        'Authorization': env.secret_key
    }
    data = {
        "config": use_config()
    }
    response = requests.post(SERVER_URL, headers=headers, data=data)
    assert response.status_code == HTTPStatus.OK

def push_code():
    commit_name = input('> Please input your commit name : ')
    Popen(['git', 'add', '-A']).wait()
    Popen(['git', 'commit', '-m', '"%s"' % commit_name]).wait()
    Popen(['git', 'push', '-u', 'origin', 'master']).wait()

def main():
    upload_config()
    push_code()
