import requests
from scripts.helpers.env_to_dict import use_env
from shared.utils.constants import SERVER_URL

env = use_env()

headers = {
    'Authorization': env.secret_key
}

def main():
    response = requests.get(SERVER_URL, headers=headers)
    print('Status Code : %d' % response.status_code)
    print('Response : ')
    try:
        print(response.json())
    except:
        print(response.content)
