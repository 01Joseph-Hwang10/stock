import requests
from time import sleep
from subprocess import Popen
from http import HTTPStatus
from urllib.parse import urljoin
from shared.hooks.use_config import use_config
from scripts.helpers.env_to_dict import use_env
from scripts.health_check import main as health_check
from scripts.last_updated import update_constant

SERVER_URL = 'http://stock-env.eba-hirrdtdm.ap-northeast-2.elasticbeanstalk.com/'
URL = urljoin(SERVER_URL, '/config/upload')

def upload_config():
    env = use_env()
    headers = {
        'Authorization': env.secret_key,
        'Content-Type': 'application/json',
    }
    data = {
        "config": use_config()
    }
    response = requests.post(URL, headers=headers, data=data)
    try:
        assert response.status_code == HTTPStatus.OK
        print('Upload was successful!')
    except:
        print('Upload was failed! (Status Code : %d)' % response.status_code)
        print('Response : ')
        print(response.content)

def push_code():
    update_constant()
    commit_name = input('> Please input your commit name : ')
    Popen(['git', 'add', '-A']).wait()
    Popen(['git', 'commit', '-m', '"%s"' % commit_name]).wait()
    Popen(['git', 'push', '-u', 'origin', 'master']).wait()

def main():
    push_code()
    print('Wating For the health check...')
    for _ in range(10):
        sleep(1000)
        if health_check():
            break
    upload_config()
